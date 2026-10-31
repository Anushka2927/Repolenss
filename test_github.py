from services.github_service import clone_repository

url = "https://github.com/pallets/flask"

try:
    path = clone_repository(url)
    print("Repository downloaded successfully!")
    print("Location:", path)

except Exception as error:
    print("Error:", error)