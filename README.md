# Basic Instrctions

To run the first version of the Hangman game, just execute:

`python3 hangman_exe.py`

This is a simple console game.

In order to run the web version, execute:

`python manage.py runserver`


# **Project SetUp**

To create a virtual environment, use the following command, where `".venv"` is the name of the environment folder:

`python3 -m venv .venv`

* Activate the virtualenv (OS X & Linux):

`source .venv/bin/activate`

You’ll need to activate your virtual environment every time you work on your Python project. In the rare cases when you want to `deactivate` your virtualenv without closing your terminal session, just use the deactivate command.

## **Package and Dependency Manager**

To install the package, you can just run:

`pip3 install <somepackage>` 

That will build an extra Python library in your home directory.

Running 'pip freeze',can help to check installed packages and packages versions listed in case-insensitive sorted order.

Save all the packages in the file with:

`pip freeze > requirements.txt`.

Add `requirements.txt` to the root directory of the project. Done.

If you’re going to share the project you will need to install dependencies by running

`pip install -r requirements.txt`

The recipient still needs to create their own virtual environment, however.

**OBS:** Use `pip3 install -r requirements.txt` if you are using Python3

# **Google Style Guides**

For this project I am going to follow Google Style Guides convention. It is much easier to understand a large codebase when all the code in it is in a consistent style.

## **YAPF - Yet Another Python Formatter**

Most of the current formatters for Python --- e.g., autopep8, and pep8ify --- are made to remove lint errors from code. This has some obvious limitations. For instance, code that conforms to the PEP 8 guidelines may not be reformatted. But it doesn't mean that the code looks good.

In essence, the algorithm takes the code and reformats it to the best formatting that conforms to the style guide, even if the original code didn't violate the style guide. 

The goal using it is to end all holy wars about formatting - if the whole codebase of a project is simply piped through YAPF whenever modifications are made, the style remains consistent throughout the project and there's no point arguing about style in every code review.

The ultimate goal is that the code YAPF produces is as good as the code that a programmer would write if they were following the style guide. It takes away some of the drudgery of maintaining your code.

To install YAPF from PyPI:

`$ pip3 install yapf`

Usage: `yapf -i {source_file_or_directory}`

here `-i` is to make changes to files in place.

## **Pylint**

Pylint is a python linter which checks the source code and also acts as a bug and quality checker. It has more verification checks and options than just PEP8(Python style guide).

This is the most commonly used tool for linting in python.

* It includes the following features:
* Checking the length of each line
* Checking if variable names are well-formed according to the project’s coding standard
* Checking if declared interfaces are truly implemented.

`pip3 install pylint`

## **Installing Flake8**

Flake8 is just a wrapper around pyflakes, pycodestyle and McCabe script (circular complexity checker) (which is used to detect complex-code).

If we like Pyflakes but also want stylistic checks, we can use flake8, which combines Pyflakes with style checks against PEP 8.

`pip3 install flake8`

# **Game API**


# **Install Django**

`pip3 install Django`

## **Creating a Project**

`django-admin startproject <my-project-name> .`

This will create a **my-project-name** directory in your current directory.

# **The development server**

Let’s verify your Django project works.

`python manage.py runserver`

You’ve started the Django development server, a lightweight Web server written purely in Python.

### **Changing the Port**

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

`python manage.py runserver 8080`

If you want to change the server’s IP, pass it along with the port. So to listen on all public IPs (useful if you want to show off your work on other computers on your network), use:

`python manage.py runserver 0.0.0.0:8000`

## Creating an app

To create your app, make sure you’re in the same directory as manage.py and type this command:

`python manage.py startapp <app-name>`

## **Use the collectstatic command**

For production deployments, you typically collect all the static files from your apps into a single folder using the python manage.py collectstatic command. You can then use a dedicated static file server to serve those files, which typically results in better overall performance. The following steps show how this collection is made, although you don't use the collection when running with the Django development server.

1. In `works_single_view/settings.py`, add the following line that defines a location where static files are collected when you use the `collectstatic` command:

`STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')`

2. In the Terminal, run the command `python manage.py collectstatic` and observe that `works_single_view_app/site.css` is copied into the top level `static_collected` folder alongside `manage.py`.

3. In practice, run `collectstatic` any time you change static files and before deploying into production.


## **Work With Data, Data Models, and Migrations**

Many web apps work with information stored in a database, and Django makes it easy to represent the objects in that database using models. In Django, a model is a Python class, derived from `django.db.models.Model`, that represents a specific database object, typically a table. You place these classes in an app's `models.py` file.

With Django, your work with your database almost exclusively through the models you define in code. Django's "migrations" then handle all the details of the underlying database automatically as you evolve the models over time. The general workflow is as follows:

1. Make changes to the models in your `models.py` file.
2. Run `python manage.py makemigrations` to generate scripts in the migrations folder that migrate the database from its current state to the new state.
3. Run `python manage.py migrate` to apply the scripts to the actual database.

