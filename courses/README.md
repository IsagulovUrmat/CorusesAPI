# Courses
***
A simple API for users to view and create various courses
***
# Getting started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
***
# Prerequisites
This is a project written using Python, Django and Django Rest Framework
***
#### 1. Сreating a folder
>On the desktop, create the test-project folder
***
#### 2. Terminal

##### In your terminal:
>Open a terminal and write commands:
>cd Desktop/test-project or cd 'Desktop'/test-project
****
#### 3. Clone the repository
```
https://github.com/IsagulovUrmat/CorusesAPI.git
```
***
#### 4. Create the virtual enviroment
```
python3 -m venv venv
source myvenv/bin/activate
```
***
#### 5. Install the requirements
```
pip install -r requirements.txt
```
***
#### 6. Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
***
#### 7. Create a new superuser
```
python manage.py createsuperuser
```
***
#### 8. Run the server
```
python manage.py runserver
```
***
# Built With

> ### `Django` - The framework used
> ### `Django Rest Framework` - The toolkit used to build API
> ### `Swagger UI` - for API documentation

## Documentation
To get the documentation go to https://courses31.docs.apiary.io/