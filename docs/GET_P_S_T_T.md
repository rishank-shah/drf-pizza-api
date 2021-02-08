# List Of Pizzas, Sizes, Types and Toppings

    GET /api/pizza/
    
Returns a list of Pizzas , sizes, types and toppings stored in Database.

## Example
### Request
    GET http://localhost:8000/api/pizza/

### Response
``` json
{
    "pizzas": [
        {
            "id": 1,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": [
                {
                    "id": 8,
                    "topping": "Capsicum"
                },
                {
                    "id": 9,
                    "topping": "Tomato"
                }
            ]
        }
    ],
    "pizza_sizes": [
        {
            "pizza_size": "Small"
        }
    ],
    "pizza_types": [
        "Regular",
        "Square"
    ]
}
```
