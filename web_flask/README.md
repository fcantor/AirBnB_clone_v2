# 0x04. AirBnB clone - Web framework

The purpose of this project is to master the following concepts:
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

## Requirements
### Python Scripts
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### HTML/CSS Files
- Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
- All your CSS files should be in the styles folder
- All your images should be in the images folder
- You are not allowed to use !important or id (#... in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on Chrome 56.0.2924.87.
- No cross browsers

---
File | Task
---|---
__init__.py | Initialize Python packages
0-hello_route.py | Script that starts a Flask web application
1-hbnb_route.py | Script that starts a Flask web application, with two routes
2-c_route.py | Script that starts a Flask web application, with three routes
3-python_route.py | Script that starts a Flask web application, with four routes
4-number_route.py | Script that starts a Flask web application, with five routes
5-number_template.py | Script that starts a Flask web application, with six routes
6-number_odd_or_even.py | Script that starts a Flask web application, with seven routes
7-states_list.py | Script that starts a Flask web application; added method @app.teardown_appcontext
8-cities_by_states.py | Script that starts a Flask web application; Route ```/citites_by_states``` displays an HTML page
9-states.py | Script that starts a Flask web application; Route ```/states``` and ```/states/<id>``` displays an HTML page
10-hbnb_filters.py | Script that starts a Flask web application; Route ```/hbnb_filters``` displays an HTML page like ```6-index.html``` from 0x01 AirBnB clone - Web Static

## Author
Francesca Cantor