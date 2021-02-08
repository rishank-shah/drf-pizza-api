from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import PizzaModel,Topping,PizzaSize
from .serializers import PizzaSerializer,ToppingSerializer,PizzaSizeSerializer

list_types = ['Regular','Square']

class PizzaViewSet(viewsets.ModelViewSet):
    '''
        Request should be like : 
        {
            "pizza_type":"Regular or Sqaure",
            "pizza_size":"<NAME_OF_SIZE>",
            "toppings":[
                {
                    "topping":"<NAME_OF_TOPPING>"
                },
                {
                    "topping":"<NAME_OF_TOPPING>"
                }
            ]
        }
    '''
    serializer_class = PizzaSerializer

    def get_queryset(self):
        pizza = PizzaModel.objects.all()[::-1]
        return pizza
    
    def list(self, request, *args, **kwargs):
        # Checking for filtering of pizza by type and size
        pizza_type = self.request.query_params.get('pizza_type', '')
        pizza_size = self.request.query_params.get('pizza_size', '')
        
        if len(pizza_type) == 0:
            pizza_type = None
        if len(pizza_size) == 0:
            pizza_size = None

        # if both paramters are present in url
        if pizza_type is not None and pizza_size is not None:
            filtered = PizzaModel.objects.filter(pizza_size__pizza_size__iexact=pizza_size).filter(pizza_type__iexact=pizza_type)
            filter_pizza_result_count = filtered.count()
            serializer = PizzaSerializer(filtered,many=True)
            return Response({
                'filter_paramters':['pizza_size','pizza_type'],
                'filter_value':[pizza_size,pizza_type],
                'filter_pizza_result_count':filter_pizza_result_count,
                'filter_pizza_result':serializer.data
            })

        #  if only pizza_size is present
        elif pizza_size is not None:
            filtered_size = PizzaModel.objects.filter(pizza_size__pizza_size__iexact=pizza_size)
            serializer_pizza_size = PizzaSerializer(filtered_size,many=True)
            return Response({
                'filter_paramter':'pizza_size',
                'filter_value':pizza_size,
                'filter_pizza_result':serializer_pizza_size.data
            })
        
        # if only pizza_type is present
        elif pizza_type is not None:
            filtered_type = PizzaModel.objects.filter(pizza_type__iexact=pizza_type)
            serializer_pizza_type = PizzaSerializer(filtered_type,many=True)
            return Response({
                'filter_paramter':'pizza_type',
                'filter_value':pizza_type,
                'filter_pizza_result':serializer_pizza_type.data
            })

        # if neither pizza_type nor pizza_size is present
        if pizza_size is None and pizza_type is None:
            serializer_topping = ToppingSerializer(Topping.objects.all()[::-1],many=True)
            serializer_size = PizzaSizeSerializer(PizzaSize.objects.all()[::-1],many=True) 
            queryset = self.filter_queryset(self.get_queryset())
            serializer_pizza = PizzaSerializer(queryset,many=True)
            return Response({
                'pizzas':serializer_pizza.data,
                'toppings':serializer_topping.data,
                'pizza_sizes':serializer_size.data,
                'pizza_types':list_types
            })

    def create(self,request,*args, **kwargs):
        data = request.data
        try:
            pizza_size = data.get('pizza_size',0)
            pizza_type = data.get('pizza_type',0)

            if pizza_size == 0 or pizza_type == 0:
                return Response({
                    'error':'Please provide pizza_size and pizza_type'
                },status=status.HTTP_400_BAD_REQUEST)
            
            pizza_type = pizza_type.lower().capitalize()
            
            if not pizza_type in list_types:
                return Response({
                    'error':'Please provide correct pizza_type',
                    'correct_type_choices':list_types
                },status=status.HTTP_400_BAD_REQUEST)

            if not PizzaSize.objects.filter(pizza_size__iexact=pizza_size).exists():
                serializer_size = PizzaSizeSerializer(PizzaSize.objects.all(),many=True) 
                return Response({
                    'error':'Please provide correct pizza_size',
                    'correct_size_choices':serializer_size.data
                },status=status.HTTP_400_BAD_REQUEST)

            pizza_size_object = PizzaSize.objects.get(pizza_size__iexact=pizza_size)
            new_pizza = PizzaModel.objects.create(pizza_size=pizza_size_object,pizza_type=pizza_type)
            
            toppings = data.get('toppings',0)
            if not toppings == 0:
                for top in toppings:
                    topping = top.get("topping")
                    if  Topping.objects.filter(topping__iexact = topping).exists():
                        top_object = Topping.objects.get(topping__iexact = topping)
                        new_pizza.pizza_toppings.add(top_object)
                    else:
                        new_pizza.delete()
                        data_topping = ToppingSerializer(Topping.objects.all(),many=True).data
                        return Response({
                            'error':f'Please enter correct topping. ({topping}) is not a valid  topping.',
                            'correct_topping_choices':data_topping
                        },status=status.HTTP_400_BAD_REQUEST)

            new_pizza.save()
            serializer = PizzaSerializer(new_pizza)
            return Response({
                'new_pizza':serializer.data
            },status = status.HTTP_201_CREATED)
        except:
            return Response({
                'error':'Something went wrong. Please try again.'
            },status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,*args, **kwargs):
        # get pizza by ID
        pizza_id = kwargs['pk']
        try:
            if not PizzaModel.objects.filter(id=pizza_id).exists():
                return Response({
                'error':"Pizza with specified id doesn't exist."
            },status=status.HTTP_400_BAD_REQUEST)

            pizza = PizzaModel.objects.get(id=pizza_id)
            serializer = PizzaSerializer(pizza)
            return Response({
                'success':'Pizza Exists',
                'pizza':serializer.data
            },status=status.HTTP_200_OK)
        except:
            return Response({
                'error':'Something went wrong. Please try again.'
            },status=status.HTTP_400_BAD_REQUEST)
           
        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args, **kwargs):
        pizza_id = kwargs['pk'] 
        try:
            if not PizzaModel.objects.filter(id=pizza_id).exists():
                return Response({
                'error':"Pizza with specified id doesn't exist."
            },status=status.HTTP_400_BAD_REQUEST)

            pizza = PizzaModel.objects.get(id=pizza_id)
            pizza.delete()
            return Response({
                'success':'Pizza Deleted'
            },status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({
                'error':'Something went wrong. Please try again.'
            },status=status.HTTP_400_BAD_REQUEST)

        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,*args, **kwargs):
        pizza_id = kwargs['pk'] 
        try:
            if not PizzaModel.objects.filter(id=pizza_id).exists():
                return Response({
                'error':"Pizza with specified id doesn't exist."
            },status=status.HTTP_400_BAD_REQUEST)

            pizza = PizzaModel.objects.get(id=pizza_id)
            data = request.data
            pizza_type = data.get('pizza_type',0)
            pizza_size = data.get('pizza_size',0)
            toppings = data.get('toppings',0)

            if pizza_type == 0:
                pizza_type = pizza.pizza_type
            else:
                pizza_type = pizza_type.lower().capitalize()
                if not pizza_type in list_types:
                    return Response({
                        'error':'Please provide correct pizza_type',
                        'correct_type_choices':list_types
                    },status=status.HTTP_400_BAD_REQUEST)

            if pizza_size == 0:
                pizza_size_object = pizza.pizza_size
            elif not PizzaSize.objects.filter(pizza_size__iexact=pizza_size).exists():
                serializer_size = PizzaSizeSerializer(PizzaSize.objects.all(),many=True) 
                return Response({
                    'error':'Please provide correct pizza_size',
                    'correct_size_choices':serializer_size.data
                },status=status.HTTP_400_BAD_REQUEST)
            else:
                pizza_size_object = PizzaSize.objects.get(pizza_size__iexact=pizza_size)
            
            if toppings == 0 :
                toppings = pizza.pizza_toppings
            else:
                pizza.pizza_toppings.clear()
                for top in toppings:
                    topping = top.get("topping")
                    if  Topping.objects.filter(topping__iexact = topping).exists():
                        top_object = Topping.objects.get(topping__iexact = topping)
                        pizza.pizza_toppings.add(top_object)
                    else:
                        data_topping = ToppingSerializer(Topping.objects.all(),many=True).data
                        return Response({
                            'error':f'Please enter correct topping. ({topping}) is not a valid  topping.',
                            'correct_topping_choices':data_topping
                        },status=status.HTTP_400_BAD_REQUEST)

            pizza.pizza_type = pizza_type
            pizza.pizza_size = pizza_size_object
            pizza.save()
            ser_pizza = PizzaSerializer(pizza)
            return Response({
                'success':'Pizza Updated Successfully',
                'updated_pizza':ser_pizza.data
            },status=status.HTTP_200_OK)
        except:
            return Response({
                'error':'Something went wrong. Please form the request body correctly.'
            },status=status.HTTP_400_BAD_REQUEST)

        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)

class ToppingViewSet(viewsets.ModelViewSet):
    '''
        Request Should Be like: {
            "topping": <NAME_OF_TOPPING>
        }
    '''
    serializer_class = ToppingSerializer

    def get_queryset(self):
        topping = Topping.objects.all()[::-1]
        return topping
    
    def create(self,request,*args, **kwargs):
        data = request.data
        try:
            topping = data.get('topping',0)
            
            if topping == 0:
                return Response({
                    'error':'Please provide topping'
                },status=status.HTTP_400_BAD_REQUEST)
            
            topping = topping.lower().capitalize()

            if Topping.objects.filter(topping__iexact=topping).exists():
                serializer_topping = ToppingSerializer(Topping.objects.all(),many=True) 
                return Response({
                    'error':f'({topping}) already exists in system',
                    'topping_existing':serializer_topping.data
                },status=status.HTTP_400_BAD_REQUEST)

            new_topping = Topping.objects.create(topping=topping)
            new_topping.save()
            serializer = ToppingSerializer(new_topping)
            return Response({
                'new_topping':serializer.data
            },status = status.HTTP_201_CREATED)
        except:
            return Response({
                'error':'Something went wrong. Please try again.'
            },status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)

class PizzaSizeViewSet(viewsets.ModelViewSet):
    '''
        Request Should Be like: {
            "pizza_size": <NAME_OF_SIZE>
        }
    '''
    serializer_class = PizzaSizeSerializer

    def get_queryset(self):
        size = PizzaSize.objects.all()[::-1]
        return size
    
    def create(self,request,*args, **kwargs):
        data = request.data
        try:
            pizza_size = data.get('pizza_size',0)
            
            if pizza_size == 0:
                return Response({
                    'error':'Please provide pizza_size'
                },status=status.HTTP_400_BAD_REQUEST)
            
            pizza_size = pizza_size.lower().capitalize()

            if PizzaSize.objects.filter(pizza_size__iexact=pizza_size).exists():
                serializer_size = PizzaSizeSerializer(PizzaSize.objects.all(),many=True) 
                return Response({
                    'error':f'({pizza_size}) already exists in system',
                    'pizza_size_existing':serializer_size.data
                },status=status.HTTP_400_BAD_REQUEST)

            new_pizza_size = PizzaSize.objects.create(pizza_size=pizza_size)
            new_pizza_size.save()
            serializer = PizzaSizeSerializer(new_pizza_size)
            return Response({
                'new_pizza_size':serializer.data
            },status = status.HTTP_201_CREATED)
        except:
            return Response({
                'error':'Something went wrong. Please try again.'
            },status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
                'error':'Unexpected Behaviour'
            },status=status.HTTP_400_BAD_REQUEST)
    