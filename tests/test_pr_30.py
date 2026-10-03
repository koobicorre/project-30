from src.pr_30 import StudentProjectManager


def test_add_project():
    manager = StudentProjectManager()

    project = manager.add_project(
        "Kristina",
        "DevOps Project"
    )

    assert project["student"] == "Kristina"
    assert project["title"] == "DevOps Project"
    assert project["status"] == "Planned"


def test_get_project():
    manager = StudentProjectManager()

    manager.add_project(
        "Kristina",
        "CI/CD Project"
    )

    project = manager.get_project("CI/CD Project")

    assert project is not None
    assert project["student"] == "Kristina"


def test_update_status():
    manager = StudentProjectManager()

    manager.add_project(
        "Kristina",
        "DevOps Project"
    )

    result = manager.update_status(
        "DevOps Project",
        "Completed"
    )

    assert result is True

    project = manager.get_project("DevOps Project")

    assert project["status"] == "Completed"


def test_project_not_found():
    manager = StudentProjectManager()

    project = manager.get_project(
        "Unknown Project"
    )

    assert project is None