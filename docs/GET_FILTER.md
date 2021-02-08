# Fiter by Pizza size and type

    GET /api/pizza/?pizza_type=regular&pizza_size=small
    
Returns a list of filtered pizza.

## Parameters

### URL Parameters
Field  | Type |Description
---  | --- | ---
pizza_type | String |Type of Pizza to be filtered with (eg:- Regular or square)
pizza_size  | String |Size of Pizza to be filtered with  (eg:- small, large, etc)

If one of them is provided like `` /api/pizza/?pizza_type=regular`` then also it will work server will not send error.

## Example
### Request

    GET http://localhost:8000/api/pizza/?pizza_type=regular&pizza_size=small

### Response
``` json
{
    "filter_paramters": [
        "pizza_size",
        "pizza_type"
    ],
    "filter_value": [
        "small",
        "regular"
    ],
    "filter_pizza_result_count": 3,
    "filter_pizza_result": [
        {
            "id": 9,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": []
        },
        {
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
        },
        {
            "id": 15,
            "pizza_type": "Regular",
            "pizza_size": {
                "id": 1,
                "pizza_size": "Small"
            },
            "pizza_toppings": []
        }
    ]
}
```
### If there is no result in database matching the filters then server will return an empty array 
### Request

    GET http://localhost:8000/api/pizza/?pizza_type=regula

### Response
``` json
{
    "filter_paramter": "pizza_type",
    "filter_value": "regula",
    "filter_pizza_result": []
}
```
