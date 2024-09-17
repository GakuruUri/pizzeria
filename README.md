```
1. Pizzeria: Start a new project called pizzeria_project with an app called 
pizzas. 
2. Define a model Pizza with a field called name, which will hold name
values, such as Hawaiian and Meat Lovers. 
3. Define a model called Topping with
fields called pizza and name. The pizza field should be a foreign key to Pizza,
and name should be able to hold values such as pineapple, Canadian bacon, and 
sausage.
4. Register both models with the admin site, and use the site to enter some 
pizza names and toppings. Use the shell to explore the data you entered.
```
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
