## Overview
You have to create a Django application which should be able to store information about different types of Pizza, then create an API interface that lists the information about all the different stored pizzas, and also be able to interact with that information (such as edit or delete).
## Database
PostgreSQL should be configured with the project. Our database should be able to store information about Pizza, following are the details :
- [x]  A Pizza can be of multiple types : Regular or Square
- [x]  A Pizza can be of multiple sizes : Small, Medium, Large, etc. (These are just examples, the user should be allowed to add any other size at any point of time)
- [x]  A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.), the choice of toppings should not be limited to the ones mentioned above, the user should be allowed to add any type of topping at any point of time)

## API
- [x]  Create an API endpoint to create regular pizza and a square pizza.
- [x]  Create an API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
- [x]  Allow filtering the list of pizza returned by the API based on Size & Type of Pizza.
- [x]  Create an API endpoint that allows the user to edit or delete any pizza from the database.

## Errors & Validation

- [x] The API should return proper 40x codes when any kind of wrong input is sent to the API, the server should not return 500 errors

- [x]  The user should not be able to create a pizza of any other type except Regular and Square.
- [x]  The user should not be able to create pizza of size which isn't present in the database.

------------

### Requirements for running project 
- [python3.8.2 (32-bit)](https://www.python.org/downloads/release/python-382/)
-  [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [git-bash](https://git-scm.com/downloads)
- [postgresql](https://www.postgresql.org/download/)

##### NOTE: If running on windows please use git-bash don't use cmd.
### Steps to run the project:
```
git clone https://github.com/rishank-shah/drf-pizza-api.git
cd drf-pizza-api
cp .env.example .env
```
##### Fill the .env file with the correct database credentials and database name
```
virtualenv venv --python=python3.8.2
source venv/Scripts/activate
pip install -r requirements.txt
source .env
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### If all commands run successfully API will be running on PORT 8000 on localhost
[http://localhost:8000](http://localhost:8000)
Check below for API Endpoints

------------

### Api Endpoints:

#### GET 
- **[<code>GET</code> List Of Pizzas, Sizes, Types and Toppings ](docs/GET_P_S_T_T.md)**
- **[<code>GET</code> List Of Pizza Toppings ](docs/GET_P_TOPPING.md)**
- **[<code>GET</code> List Of Pizza Sizes ](docs/GET_P_SIZES.md)**
- **[<code>GET</code> Get pizza by id ](docs/GET_P_BY_ID.md)**
- **[<code>GET</code> Fiter by Pizza size and type ](docs/GET_FILTER.md)**

#### POST
- **[<code>POST</code> Create Pizza ](docs/POST_C_P.md)**
- **[<code>POST</code> Create Pizza Size ](docs/POST_C_PS.md)**
- **[<code>POST</code> Create Pizza Toppings ](docs/POST_C_PT.md)**

#### PUT
- **[<code>PUT</code> Update Pizza ](docs/PUT_P.md)**

#### DELETE
- **[<code>DELETE</code> Delete Pizza ](docs/DELETE_P.md)**
