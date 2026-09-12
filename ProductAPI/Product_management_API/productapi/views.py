
from .models import Products
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def products_list_view(request):
    if request.method == "GET":
        products = Products.objects.all()

        PRODUCTS = []

        for product in products:
            product_dict = {

            'name' : product.name,
            'price' : product.price,
            'quantity' : product.quantity,
            'brand': product.brand,
            }

            PRODUCTS.append(product_dict)

        json_data = json.dumps(PRODUCTS)


        return HttpResponse(json_data,content_type= 'application/json',status = 200)
    
    if request.method == "POST":
        request_data = json.loads(request.body)

        product = Products.objects.create(**request_data)

        python_data = {
            'message':'Porduct created successfully',
            'data':{

                'name' : product.name,
                'price' : product.price,
                'quantity' : product.quantity,
                'brand': product.brand,

            }
        }

        response_data = json.dumps(python_data)

        return HttpResponse(response_data,content_type = 'application/json',status = 201)

    python_data = {
        'errors':'only get and post methods are allowed'
    }
    response_data = json.dumps(python_data)
    return HttpResponse(response_data,content_type = 'application/json',status =405)
       



def products_details_view(request,product_id):
    try:
        product = Products.objects.get(id = product_id)
    except Products.DoesNotExist:
        python_data = {
            'error':'Product does not exist'
        }
        request_data = json.dumps(python_data)
        return HttpResponse(request_data,content_type = 'application/json',status = 200 )

    if request.method =='GET':
        python_data = {
            'message':'Product found successfully',
            'data':{
                'name' : product.name,
                'price' : product.price,
                'quantity' : product.quantity,
                'brand': product.brand,
                
            }
        }
        response_data = json.dumps(python_data)
        return HttpResponse(response_data,content_type = 'application/json',status = 200)


    if request.method =='PUT':
                                                                                                                     


    