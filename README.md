# Reaktor-Assignment-2022: Poetry.lock Parser App
This repository contains my solution for the Reaktor Software Developer Trainee, Autumn 2022 [pre-assignment](https://www.reaktor.com/assignment-fall-2022-developers/).

> Some Python projects use Poetry to manage dependencies. Poetry uses a file called poetry.lock to record which packages a project needs and which dependencies those packages have. Here is an example of such a file. Write a small program in your language of choice that accepts a poetry.lock file as input and exposes some key information about the packages via an HTML user interface.

## My implementation

My implementation of the assignment is testable on [Heroku](https://poetry-lock-parser-app.herokuapp.com/).

My solution is a simple web application that is written mainly in Python and uses [Flask](https://www.fullstackpython.com/flask.html) as the web framework. The app consists of two main packages, _parsing_ and _ui_, and a short script _app.py_. 

### [parsing](https://github.com/oliviahorjamo/Reaktor-Assignment-2022/tree/main/parsing)

- _parser.py_: Handles all parsing of a poetry.lock file that it is given. Returns a list of all packages in the file as ParsedPackage objects.
- _parsed_package.py_: Includes the code for the class ParsedPackage that represents a parsed package.

### [ui](https://github.com/oliviahorjamo/Reaktor-Assignment-2022/tree/main/ui)

- _src_ -folder includes _routes.py_ that renders html -templates, handles form inputs and redirects the user
- _templates_ -folder includes all html -templates that the app uses. They are written mainly in html with a tiny bit of JavaScript included.
- _static_ -folder includes _style.css_ that dictates how the html templates are to be shown.

### [app.py](https://github.com/oliviahorjamo/Reaktor-Assignment-2022/blob/main/app.py)

- This module is placed in the main folder and includes the code that is needed to get the app up and running.
