
from services.github_service import clone_repository
from services.graph_service import get_graph_summary
from services.ai_service import analyze_repository

repo_url = "https://github.com/pallets/flask"

try:
    print("Fetching repository...")
    repo_path = clone_repository(repo_url)

    print("\nLoading Graphify analysis...")
    graph_summary = get_graph_summary(repo_path)

    print("\nSending repository information to Gemma AI...")
    ai_result = analyze_repository(graph_summary)

    print("\n" + "=" * 50)
    print("REPOLENS AI REPOSITORY ANALYSIS")
    print("=" * 50)

    print(ai_result)

except Exception as error:
    print("\nERROR:", error)
