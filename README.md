## Table of content
- [Description](#description)
- [Tools](#tools)
- [Running](#running)

## Description
Flask App Template is a project to be used as a template for those who wants to speedy it up flask applications set up.
It also supports PostgreSQL database set up.

## Tools

- [Flask](https://flask.palletsprojects.com/) with some extensions to supporting Postgresql:
    - [Flask Migrate](https://flask-migrate.readthedocs.io/)
    - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)
- [Marshmallow](https://marshmallow.readthedocs.io/) for validating body and query string requests
- [Pytest](https://docs.pytest.org/) for testing

## Running

1. Rename with your application
    ```sh
    $ ./rename_project.sh application_name
    ```

2. Make all adjustments you think are necessary

3. I strongly recommend using virtualenvs
    ```sh
    $ python -m venv /path/to/virtualenv/application_name
    $ source /path/to/virtualenv/application_name/bin/activate
    ```

4. Install dependencies
    ```sh
    $ pip install -r requirements.txt
    ```

5. Run server
    ```sh
    $ python app.py
    ```

6. Access the application on http://localhost:3000
