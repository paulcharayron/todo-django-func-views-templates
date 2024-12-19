# todo-django-func-views-templates

A simple todo app, written in Python with the Django framework, using function-based views and templates.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Important Notes](#important-notes)

## Prerequisites

1. Access to Docker Hub, and Docker installed on your machine

## Installation

1. Clone the repository:

```bash
 git clone https://github.com/paulcharayron/todo-django-func-views-templates.git
```

## Usage

To run the project, use the following command (from the root of the project):

```bash
docker-compose up
```

## Important Notes

If you deploy this project on the Internet, please make sure to:

- Change your Django SECRET_KEY and reference an environment variable, rather than using raw value in settings.py
- Reference environment variables for the environment variables of the services in docker-compose.yml

## License

This project is licensed under the [MIT License](https://opensource.org/license/MIT).
