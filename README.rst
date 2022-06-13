.. role:: python(code)
   :language: python

########################################
Resource manager -> Scooter Manager
########################################

Compatible with:

- **django**: 4.0.2
- **djangorestframework**: 3.13.1
- **psycopg2-binary**: 2.9.3
- **drf-yasg**: 1.20.0
- **postgreSQL**: 12.11
- **docker**: 20.10.7

- **Django Rest Framework**: 3.10, 3.11, 3.12

This application provides an api for managing a scooter rental company, being possible to create users within the system to register products and manipulate them (admins) and create users to rent the products (common users)

********
Features
********

- full scooter management (admin users)
- full user management (admin users)
- scooter rental (regular users)
- token based authentication
- the system does not allow two vehicles with the same license plate
- the system does not allow regular users to update the name, id or license plate of scooters
- the system does not allow regular users to assign their rent to another user
- the system does not allow updating the rental data (rent_date, end_rent_date, user)
- the system does not allow regular users to delete scooters, only admin users

*****************
Table of contents
*****************

.. contents::
   :depth: 4

*****
Usage
*****

0. Installation
===============

OBS: to install and run this project you must have postgreSQL installed and a database called resource-manager


first go to the /resource_manager/settings.py directory in the following code snippet insert:

.. code:: python

   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'resource_manager', 
        'USER': 'postgres', 
        'PASSWORD': '{put your password here!}',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
      }
    }

with the database properly configured, let's create an env to run our application in an isolated environment:

.. code:: console

  python -m venv venv

then we will activate the virtual env

.. code:: console

  . venv/bin/activate

or 

.. code:: console

  source venv/bin/activate

if you are in a windows environment, run the following command:

.. code:: console

  source venv/scripts/activate

With your virtual env activated, let's now install pipenv so that it can install our dependencies

.. code:: console
   
   pip install pipenv

Now we will install all project dependencies with the command:

.. code:: console
   
   pipenv install

With everything properly installed, it's time to upload the migrations of our database in our project, for that, run the following commands in your terminal:

.. code:: console
   
   python manage.py makemigrations

and then:

.. code:: console
   
   python manage.py migrate

finally, let's start our application

.. code:: console
   
   python manage.py runserver


1. Installation with Docker
===============
To run this program with docker is very simple, just run the following command:

.. code:: console

   docker-compose up --build
   

2. Quickstart
=============

with the project running access the link:

.. code:: console

http://localhost:8000/

or the following link to a documentation on the swagger model: 
 
.. code:: console

http://localhost:8000/swagger/

To make good use of this project, import the **scooter_rent.postman_collection.json file into your **POSTMAN** and enjoy! 

########################################

**This app was created by Lucas Amorim (Little Love) 🧑‍💻🦆🐍🐉**
