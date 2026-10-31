
import streamlit as st
import json
from pathlib import Path

st.set_page_config(
    page_title="RepoLens",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 RepoLens")
st.subheader("AI-Powered GitHub Repository Analyzer")

st.write(
    "Understand any GitHub repository using "
    "Graphify and Gemma AI."
)

repo_url = st.text_input(
    "Enter GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Analyze Repository"):
    if repo_url.strip():
        st.info("Repository analysis will start here.")
    else:
        st.warning("Please enter a GitHub URL.")

# Locate existing Graphify output
graph_path = (
    Path(__file__).resolve().parent.parent
    / "graphify-out"
    / "graph.json"
)

st.divider()
st.header("Repository Knowledge Graph")

if graph_path.exists():
    with open(graph_path, "r", encoding="utf-8") as file:
        graph = json.load(file)

    nodes = graph.get("nodes", [])
    links = graph.get("links", [])
    hyperedges = graph.get("hyperedges", [])

    col1, col2, col3 = st.columns(3)

    col1.metric("Nodes", len(nodes))
    col2.metric("Connections", len(links))
    col3.metric("Communities",
                len(set(n.get("community")
                        for n in nodes
                        if n.get("community") is not None)))

    st.subheader("Graph Nodes")

    st.dataframe(
        [
            {
                "Name": node.get("label"),
                "Type": node.get("file_type"),
                "Community": node.get("community_name"),
                "Source": node.get("source_file")
            }
            for node in nodes
        ],
        use_container_width=True
    )

    st.subheader("Graph Relationships")
    st.json(links)

    st.subheader("Hyperedges")
    st.json(hyperedges)

else:
    st.warning("Graphify output not found.")

st.divider()
st.caption("RepoLens | AI-powered developer intelligence")
