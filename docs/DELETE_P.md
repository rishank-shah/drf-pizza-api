# Delete Pizza

    DELETE /api/pizza/:pizza_id/
    
Delete Pizza of specified ID.

## Parameters
### URL Parameters
http://localhost:8000/api/pizza/:pizza_id/
pizza_id -> Pizza object id

## Example
### Request

    DELETE http://localhost:8000/api/pizza/9/

### Response
``` json
{
    "success": "Pizza Deleted"
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
