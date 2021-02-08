# Pizza Sizes List

    GET /api/pizza_size/
    
Returns a list of pizza sizes in database.

## Example
### Request

    GET http://localhost:8000/api/pizza_size/

### Response
``` json
[
    {
        "pizza_size": "Large"
    },
    {
        "pizza_size": "Medium"
    },
    {
        "pizza_size": "Small"
    }
]
```