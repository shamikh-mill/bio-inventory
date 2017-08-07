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



<!-- Delete Button: form action was "{% url 'inventory:item-delete' item.id %}" -->
<!-- Edit button: form action was {% url 'inventory:item-update' item.id %} -->
{% if item.checked_out == False %}
       {% endif %}


````

## License: MIT

