# Biology IT Inventory Dashboard

Biology IT Inventory is a web platform built for the Biology IT helpdesk that allows helpdesk members to keep track of in stock and checked out laptops, chargers, cameras, and adapters and their current users. It's a user-friendly dashboard style application that supports API usage for querying in stock and out of stock items, and it's built using Django and the Django REST framework. 

## Features

- Core CRUD features 
- PostgreSQL database backend 
- REST API to get current stock and current checked out items and their details and current users 

## Installation 
1. Clone this repository

2. Run the following:

````
$ pip install -r requirements.txt
$ python manage.py runserver 
# OR 
$ heroku run python manage.py runserver
````


## Resources for reference 
1. https://medium.freecodecamp.org/how-to-understand-django-models-the-simple-way-20c39d234870

