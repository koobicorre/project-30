class StudentProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, student, title, status="Planned"):
        project = {
            "student": student,
            "title": title,
            "status": status
        }

        self.projects.append(project)

        return project

    def get_project(self, title):
        for project in self.projects:
            if project["title"] == title:
                return project

        return None

    def update_status(self, title, new_status):
        project = self.get_project(title)

        if project:
            project["status"] = new_status
            return True

        return False

    def list_projects(self):
        return self.projects