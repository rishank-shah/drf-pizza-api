# Create Pizza

    POST /api/pizza/
    
Create a Pizza. Returns the newly-created object.

## Parameters
### Body Parameters
Field | Required| Type | Description
--- | --- | --- | ---
pizza_type | Y| String | Type of pizza (It can only be Regular or Square)
pizza_size | Y |String| Size of pizza (eg:- small, large, etc)
toppings | N | Array | Toppings to put on pizza (eg:- capsicum, etc). There can be multiple toppings

## Example
### Request

    POST http://localhost:8000/api/pizza/
#### Request Body
```json 
{
	"pizza_type":"Regular",
	"pizza_size":"small",
	"toppings":[
		{
			"topping":"Capsicum"
		},
		{
			"topping":"Tomato"
		}
	]
}
```
### Response
``` json
{
    "new_pizza": {
        "id": 16,
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
#### If anything other than Regular or Square is passed for pizza_type
``` json
{
    "error": "Please provide correct pizza_type",
    "correct_type_choices": [
        "Regular",
        "Square"
    ]
}
```
#### If pizza_size is not present in database
``` json
{
    "error": "Please provide correct pizza_size",
    "correct_size_choices": [
        {
            "pizza_size": "Small"
        },
        {
            "pizza_size": "Large"
        },
        {
            "pizza_size": "Medium"
        }
    ]
}
```

#### If topping is not present in database
``` json
{
    "error": "Please enter correct topping. (cap) is not a valid  topping.",
    "correct_topping_choices": [
        {
            "topping": "Capsicum"
        },
        {
            "topping": "Tomato"
        }
    ]
}
```