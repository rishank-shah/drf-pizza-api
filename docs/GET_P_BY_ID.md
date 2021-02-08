# Display Pizza By ID

    GET /api/pizza/:pizza_id/
    
Returns a pizza by id.

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

## Example
### Request

    GET http://localhost:8000/api/pizza/10/

### Response
``` json
{
    "success": "Pizza Exists",
    "pizza": {
        "id": 10,
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
}
```
### Error
#### If pizza of mentioned id does not exist in Database then server repondes with a 400 Bad Request
### Response
``` json
{
    "error": "Pizza with specified id doesn't exist."
}
```
