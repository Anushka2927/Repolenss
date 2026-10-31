
from services.github_service import clone_repository
from services.graph_service import get_graph_summary

repo_url = "https://github.com/pallets/flask"

try:
    print("Fetching repository...")
    repo_path = clone_repository(repo_url)

    print("\nReading Graphify output...")
    summary = get_graph_summary(repo_path)

    print("\nREPOLENS GRAPH ANALYSIS")
    print("----------------------")
    print("Total Nodes:", summary["total_nodes"])
    print("Total Connections:", summary["total_connections"])
    print("Total Communities:", summary["total_communities"])
    print("Total Hyperedges:", summary["total_hyperedges"])

except Exception as error:
    print("Error:", error)
