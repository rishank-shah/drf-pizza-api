from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet,ToppingViewSet,PizzaSizeViewSet
from . import views

router = DefaultRouter()
router.register("pizza",PizzaViewSet,basename="pizza")
router.register("pizza_toppings",ToppingViewSet,basename="topping")
router.register("pizza_size",PizzaSizeViewSet,basename="size")

urlpatterns = [
    path('',include(router.urls)),
]