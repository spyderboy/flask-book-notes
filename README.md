Working example: https://jlbooks.herokuapp.com/

This project was inspired by a test task a potential employer sent me. The requirements:
* Host final project on Heroku with source code on GitHub
* Use SQLAlchemy to translate model to database entries
* Migration via Flask-Migrate
* The Flask app should have a virtualenv and a requirements.txt file that allows for the environment to be built from scratch on other systems
* The Flask application should use Blueprints and have at least one Blueprint for authentication and one Blueprint for other operations
* Use email to confirm new user registration
* Once logged in, show a list of the user's books
* Allow CRUD of Title, Author, Date Read, and Notes

In my research I stumbled on the MVP project by jelmerdejong (see below). I am working in a Windows environment and learned a few things about that. I'll write up a "Getting Started" for the Windows version soon.
----------------------------------------------------
# Flask App Blueprint: the fast way to start your MVP
[![CircleCI](https://circleci.com/gh/jelmerdejong/flask-app-blueprint.svg?style=shield)](https://circleci.com/gh/jelmerdejong/flask-app-blueprint)

Flask App Blueprint is a boilerplate / starter project that will help you get started with an easy to learn, yet powerful technology stack. A stack that you can have up and running in less than 25 minutes, so you can focus on making the real thing. Ideal for hackathons, prototypes, MVPs, idea validation, or kickstarting your startup. Including registration, login, insert and retrieve info from a database, email integration, and have it all deployed on Heroku.

Created by [@jelmerdejong](https://twitter.com/jelmerdejong).

## Features
* User registration (including email confirmation through Mandrill), forgot password
* User profiles, including change password
* Admin only pages including statistics and user management
* Public and member only pages
* Database setup, including database migrations and CRUD examples
* Fast deployment on Heroku (including staging and production setup)
* Powerful stack: back-end based on Python with Flask, front-end is Bootstrap
* Including basic testing coverage and framework (nose2), and PEP8 check (flake8)

## Documentation
Find all the documentation in this repository in the [docs folder](docs/README.md).

### [Getting Started](docs/getting-started.md)
