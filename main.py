from src.pr_30 import StudentProjectManager


manager = StudentProjectManager()

manager.add_project(
    "Kristina Vavilova",
    "DevOps CI/CD Project",
    "In Progress"
)

manager.add_project(
    "Student 2",
    "Web Application",
    "Planned"
)

print("Student Projects")

for project in manager.list_projects():
    print(
        project["student"],
        "-",
        project["title"],
        "-",
        project["status"]
    )