from src.pr_30 import StudentProjectManager


manager = StudentProjectManager()


def show_menu():
    print("\nStudent Project Management System")
    print("1. Add project")
    print("2. Show all projects")
    print("3. Find project")
    print("4. Update project status")
    print("5. Exit")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        student = input("Student name: ")
        title = input("Project title: ")
        status = input("Project status: ")

        manager.add_project(student, title, status)

        print("Project added successfully.")

    elif choice == "2":
        projects = manager.list_projects()

        if not projects:
            print("No projects found.")
        else:
            print("\nStudent Projects:")

            for project in projects:
                print(
                    project["student"],
                    "-",
                    project["title"],
                    "-",
                    project["status"]
                )

    elif choice == "3":
        title = input("Enter project title: ")

        project = manager.get_project(title)

        if project:
            print(
                project["student"],
                "-",
                project["title"],
                "-",
                project["status"]
            )
        else:
            print("Project not found.")

    elif choice == "4":
        title = input("Enter project title: ")
        new_status = input("Enter new status: ")

        if manager.update_status(title, new_status):
            print("Project status updated.")
        else:
            print("Project not found.")

    elif choice == "5":
        print("Program finished.")
        break

    else:
        print("Invalid option.")