# ⚙️ Project Configuration

#### RBAC

Role-based access control (RBAC) is a policy-neutral access-control mechanism defined around roles and privileges.

#### Flake8

Flake8 is a linting tool for Python. By providing specific configuration defined in the `.setup.cfg` file it prevents developers from making silly mistakes in their code and enforces PEP8 compliance in the codebase.

[Flake8 Configuration Example Code](../setup.cfg)

#### isort 

isort your imports, so you don't have to.

isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type. It provides a command line utility.

[isort Configuration Example Code](../setup.cfg)


#### Test Driven Development (TDD)
Test-driven development is a software development process relying on software requirements being converted to test cases before software is fully developed. [here](https://en.wikipedia.org/wiki/Test-driven_development)

#### Deployment

Heroku app is already configured to this repository for *automatic deploys* from any push to the **master** branch. Create a pull request containing your respective changes and wait for merge.

#### Coverage 

Coverage is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
[Docs](https://coverage.readthedocs.io/en/6.0.2/)

#### Continuous Integration

Continuous integration automates the building, testing and deploying of applications. Software projects, whether created by a single individual or entire teams, typically use continuous integration as a hub to ensure important steps such as unit testing are automated rather than manual processes.


#### CircleCI 

Great businesses depend on great software. No matter the size of your team, choose CircleCI's CI/CD platform to automate confidence in your code.

#### Celery - Distributed Task Queue

Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

It’s a task queue with focus on real-time processing, while also supporting task scheduling.
