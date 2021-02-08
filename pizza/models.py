from django.db import models

TYPE_CHOICE = (
    ('Regular','Regular'),
    ('Square','Square'),
)

class Topping(models.Model):
    topping = models.CharField(max_length=64, unique=True, blank=False)

    def __str__(self):
        return str(self.topping)
    
class PizzaSize(models.Model):
    pizza_size = models.CharField(max_length=50,unique=True,blank=False)

    def __str__(self):
        return str(self.size)

class PizzaModel(models.Model):
    pizza_type = models.CharField(max_length=7,blank=True,choices=TYPE_CHOICE)
    pizza_size = models.ForeignKey(PizzaSize,on_delete=models.CASCADE)
    pizza_toppings = models.ManyToManyField(Topping,blank=True)

    def __str__(self):
        return str(self.pizza_type) + '--' +str(self.pizza_size.size) + '-- Topping Number: ' + str(self.pizza_toppings.count())
