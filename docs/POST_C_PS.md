# Create Pizza Size

    POST /api/pizza_size/
    
Create a new Pizza Size.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
pizza_size | Y |String| Size of pizza (eg:- small, large, etc)

## Example
### Request

    POST http://localhost:8000/api/pizza_size/
### Request Body
```json 
{
    "pizza_size": "Medium"
}
```
### Response
``` json
{
    "new_pizza_size": {
        "pizza_size": "Medium"
    }
}
```

### Error
#### If Size already existing in Database
``` json
{
    "error": "(New) already exists in system",
    "pizza_size_existing": [
        {
            "pizza_size": "Small"
        },
        {
            "pizza_size": "New"
        }
    ]
}
```