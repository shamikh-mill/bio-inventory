# Biology IT Inventory Dashboard

A user-friendly dashboard style application to keep track of loaner equipment inventory for the Biology IT helpdesk of Duke University.  

## Features

- Postgresql database backend with core CRUD features 

## Installation 
1. Clone repo

````
$ pip install -r requirements.txt
$ python manage.py runserver 
# OR 
$ heroku run python manage.py runserver
````
{% if item.checked_out == False %}
       {% endif %}
{% url 'inventory:item-delete' item.id %}

````

## License: MIT

