# Flask-Gunicorn-Docker

Sample of Python3 Flask application with gunicorn and docker

## Table of contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Migrations](#migrations)
- [Project structure](#project structure)
- [View routes](#view routes)
- [Running](#running)

## Requirements

- Python (>=3.7.2)
- Virtualenv (>=15.1.0)
- Docker (>=18.09.2)
- docker-compose (>=1.23.2)
- node (>=8.12.0)
- npm (>=6.9.0)
- yarn (>=1.15.2)

## Installation

```bash
# Clone repository
$ git clone https://github.com/morozovcookie/flask-gunicorn-docker.git
$ cd flask-gunicorn-docker

# Create virtual environment
$ virtualenv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create database from the last migration
$ alembic upgrade head

# Install client dependencies
$ cd flask_gunicorn_docker/static
$ yarn install
```

## Configuration

|Variable name|Description|
|---|---|
|POSTGRES_MASTER_USERNAME|Login to PostgreSQL|
|POSTGRES_MASTER_PASSWORD|Password to PostgreSQL|
|POSTGRES_MASTER_HOST|Address of PostgreSQL master|
|POSTGRES_MASTER_PORT|Port of PostgreSQL master|
|POSTGRES_MASTER_DATABASE|PostgreSQL database name|
|POSTGRES_SLAVE_USERNAME|Login to PostgreSQL|
|POSTGRES_SLAVE_PASSWORD|Password to PostgreSQL|
|POSTGRES_SLAVE_HOST|Address of PostgreSQL slave|
|POSTGRES_SLAVE_PORT|Port of PostgreSQL slave|
|POSTGRES_SLAVE_DATABASE|PostgreSQL database name|

## Migrations

```bash
# Fixed model changes
$ alembic revision --autogenerate -m "<revision name>"

# Apply changes to database
$ alembic upgrade head
```

## Project structure
```bash
├── Dockerfile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── docker-compose.yml
├── flask_gunicorn_docker
│   ├── __init__.py
│   ├── api                                                             set of api
│   │   ├── __init__.py
│   │   └── users                                                       user api blueprint with routes
│   │       ├── __init__.py
│   │       ├── blueprint.py
│   │       └── views.py
│   ├── app.py
│   ├── infrastructure                                                  set of connection with infrastructure
│   │   ├── __init__.py
│   │   └── postgres.py
│   ├── repositories                                                    set of repositories for manipulating data
│   │   ├── __init__.py
│   │   └── user
│   │       ├── __init__.py
│   │       ├── model.py                                                user model
│   │       └── repository.py                                           user repository
│   ├── static                                                          client application
│   │   ├── README.md
│   │   ├── build                                                       assets for production use
│   │   │   ├── asset-manifest.json
│   │   │   ├── favicon.ico
│   │   │   ├── index.html
│   │   │   ├── manifest.json
│   │   │   ├── precache-manifest.2f58fda694e4483ca3441447ae92b570.js
│   │   │   ├── service-worker.js
│   │   │   └── static
│   │   ├── node_modules                                                nodejs dependencies
│   │   ├── package.json
│   │   ├── public                                                      client views
│   │   │   ├── favicon.ico
│   │   │   ├── index.html
│   │   │   └── manifest.json
│   │   ├── src                                                         client logic
│   │   │   ├── App.css
│   │   │   ├── App.js
│   │   │   ├── App.test.js
│   │   │   ├── index.css
│   │   │   ├── index.js
│   │   │   ├── logo.svg
│   │   │   └── serviceWorker.js
│   │   └── yarn.lock
│   ├── usecases                                                        application use cases
│   │   ├── __init__.py
│   │   └── user                                                        set use cases for interaction with user
│   │       ├── __init__.py
│   │       ├── store_user.py
│   │       └── users_list.py
│   ├── version.py
│   └── views                                                           routes for the serving views
│       ├── __init__.py
│       └── index.py
├── requirements.txt                                                    python3 project dependencies
└── venv                                                                virtual environment
```

## View routes

For the view available HTTP routes use the command:

```bash
$ flask routes
```

## Running

### Development mode

For development mode you should use two separates console. First you should run client dev server:

```bash
$ cd flask_gunicorn_docker/static
$ yarn start
```

Next in another console you should run Flask server

```bash
$ cd flask_gunicorn_docker
$ flask run
```

### Production mode

```bash
# First you need to build static files
$ cd flask_gunicorn_docker/static
$ yarn build

# Now you can run server. For the production you should use gunicorn
$ cd ..
$ gunicorn -b 0.0.0.0:80 -w 4 app:app
```

### Run tests

```bash

```
