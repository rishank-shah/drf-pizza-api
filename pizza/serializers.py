from rest_framework import serializers
from .models import PizzaModel,Topping,PizzaSize

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = PizzaModel
        fields = ['id','pizza_type','pizza_size','pizza_toppings']
        depth = 1

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['topping']

class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = ['pizza_size']
