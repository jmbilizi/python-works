# DJANGO TUTORIAL

1. Setting up dev environment

- Install python by going to python.org
- Install pipenv by running `pip3 install pipenv`
- Create the project folder and open it
- Open the project folder in the terminal and run `pipenv install django`
- Activate this project's virtualenv by running `pipenv shell`
- Use django-admin utility to interact with django. By running `django-admin` you will see all the command available in django-admin
- Start a project in our environment By running `django-admin startproject currentDirectoryName .`
- Start server by running `python manage.py runserver` or `python manage.py runserver 9000`
- To get the path to the virtual environment run `pipenv --venv`
- To run these cmds directly in VS Code integrated terminal. You need to set python interpreter to run python from our virtual environment (Open cmd Palette, search for python interpreter, click on it, then enter the path to the virtual environment following by \s\python)
- To start an app run `python manage.py startapp appname`
- Create superUser by running `python manage.py createsuperuser` and follow the steps asked

## Setting up python virtual environment

- Create forder you want to store in the virtual environment and open it with terminal cmd
- Run `python -m venv envirnmentName` to create the virtual environmrnt
- To activate the virtual environment, on windows run `venvName\Scripts\activate`, `source venv/scripts/activate` and mac run `source bin/activate`
- To deactivate run `deactivate`
- To install packages to our environment, run `pip install name-of-the-package`; eg; `pip install django`; `pip install djangorestframework mssql-django`
- To install packages from the requirements.txt file, run `pip install -r requirements.txt`
- To add packages from virtual environment file into requirements.txt file, run `pip freeze > requirements.txt`
- To install pytorch; run `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
- To see what has been install in our virtual environment, run `pip freeze`
- To upgrade pip version, run `python.exe -m pip install --upgrade pip`
