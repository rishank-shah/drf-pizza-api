# Pizza Toppings List

    GET /api/pizza_toppings/
    
Returns a list of pizza toppings in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_toppings/

### Response
``` json
[
    {
        "topping": "Tomato"
    },
    {
        "topping": "Capsicum"
    }
]
```