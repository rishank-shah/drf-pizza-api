from django.contrib import admin
from .models import PizzaModel, Topping

admin.site.register(PizzaModel)
admin.site.register(Topping)