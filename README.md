# Student Project Management System

## Description

Student Project Management System is a simple Python console application for managing student projects.

The application allows users to:

- add a student project;
- display all student projects;
- find a project by title;
- update the status of a project.

The project was created as part of the DevOps assignment to demonstrate the use of Git, GitHub, automated testing, and CI/CD with GitHub Actions.

## Technologies

- Python
- Git
- GitHub
- GitHub Actions
- pytest

## Project Structure

project-30/
│
├── src/
│   ├── __init__.py
│   └── pr_30.py
│
├── tests/
│   ├── __init__.py
│   └── test_pr_30.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Install the required dependency:

pip install -r requirements.txt

## Run

Run the application with:

python main.py

After running the program, the following menu is displayed:

1. Add project
2. Show all projects
3. Find project
4. Update project status
5. Exit

## Testing

The project contains four automated tests.

The tests check:

- adding a project;
- finding a project;
- updating the project status;
- searching for a project that does not exist.

Run the tests with:

pytest

Successful result:

4 passed

## Build

The Build stage checks the Python source files using:

python -m compileall src main.py

## CI/CD

The project uses GitHub Actions for continuous integration.

The workflow file is located at:

.github/workflows/ci.yml

The pipeline automatically starts after:

- push;
- pull request.

The pipeline consists of two main stages:

Build → Test

### Build

The Build stage:

- downloads the repository;
- installs Python;
- checks the Python source files.

### Test

The Test stage:

- downloads the repository;
- installs Python;
- installs dependencies from requirements.txt;
- automatically runs pytest.

If the Build stage is successful, the Test stage starts automatically.

The final successful result is:

Build — SUCCESS  
Test — SUCCESS  
Pipeline — SUCCESS