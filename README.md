```
1. Pizzeria: Start a new project called pizzeria_project with an app called pizzas. 

2. Define a model Pizza with a field called name, which will hold name values, such as Hawaiian and Meat Lovers. 

3. Define a model called Topping with
fields called pizza and name. The pizza field should be a foreign key to Pizza, and name should be able to hold values such as pineapple, Canadian bacon, and sausage.

4. Register both models with the admin site, and use the site to enter some pizza names and toppings. Use the shell to explore the data you entered.
```
## Setting Up a Project

1. Create a venv
-- Windows, use the command ll_env\Scripts\activate.
-- Linux use the command ll_env\bin\activate

2. Install Django
-- pip install --upgrade pip
-- pip install django

3. Creating a Project in Django
-- django-admin startproject pizza_project .
```
The dot (.) at the end of the command creates the new project
with a directory structure that will make it easy to deploy the app to a server
when we’re finished developing it.
```
4. Creating the Database
-- python manage.py migrate

5. Viewing the Project
-- python manage.py runserver


## Starting an App

<<<<<<< HEAD

=======
>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
1. startapp
-- python manage.py startapp pizza

2. Defining Models
-- Define a model Pizza
-- Define a model called Topping 

<<<<<<< HEAD
## Activating Models

1. Define a model Pizza. 
2. Define a model called Topping

-- python manage.py makemigrations pizzas
-- python manage.py migrate

## Django admin site configuration
1. Setting Up a Superuser
--python manage.py createsuperuser
=======
3. Activating Models
-- python manage.py makemigrations learning_logs
-- python manage.py migrate

4. The Django Admin Site
-- python manage.py createsuperuser


# Registering a Model with the Admin Site
>>>>>>> 2f3f196629cff24a4fe148a9e0fe5a3171560a01
