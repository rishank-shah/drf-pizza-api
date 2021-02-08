# Create Pizza Toppings

    /api/pizza_toppings/
    
Create a new Pizza Topping.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
topping | Y |String| Topping of pizza (eg:- capsicum, tomato, etc)

## Example
### Request

    POST http://localhost:8000/api/pizza_toppings/
#### Request Body
```json 
{
    "topping": "onion"
}
```
### Return
``` json
{
    "new_topping": {
        "topping": "Onion"
    }
}
```

### Error
#### If Topping already existing in Database
``` json
{
    "error": "(Capsicum) already exists in system",
    "topping_existing": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```