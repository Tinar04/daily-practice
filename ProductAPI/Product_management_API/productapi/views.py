
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
       



@csrf_exempt
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

# used to replace entire product except id
    if request.method =='PUT':
            request_data = json.loads(request.body)
            required_fields = ['name', 'price','quantity','brand']

            missing_field = []


            for field in required_fields:
                if field not in request_data:
                    missing_field.append(field)

            if missing_field:
                python_data = {
                    'errors':'missing field'
                }

                fields = {}
                for field in missing_field:
                    fields[field] = 'Field is mendatory'

                python_data['fields'] = fields

                request_data = json.dumps(python_data)

                return HttpResponse (request_data,content_type='application/json', status=400) 

            product.name = request_data.get('name')
            product.price = request_data.get('price')
            product.quantity = request_data.get('quantity')
            product.brand = request_data.get('brand')

            product.save()

            python_data = {
                'messsage':'Product replaced succefully',
                'data':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.quantity,
                    'quantity':product.brand,
                    'brand':product.brand
                }
            }
            response_data = json.dumps(python_data)
            return HttpResponse(response_data,content_type ='application/json',status=200)

    if request.method=='PATCH':
        request_data = json.loads(request.body)

        product.name = request_data.get('name',product.name)
        product.price = request_data.get('price',product.price)
        product.quantity = request_data.get('quantity',product.quantity)
        product.brand = request_data.get('brand',product.brand)

        product.save()


        python_data = {
            'message':'product updated sucessfully',
            'data':{
                'id':product.id,
                'name':product.name,
                'price':product.quantity,
                'quantity':product.brand,
                'brand':product.brand
            

            }
        }

        response_data = json.dumps(python_data)
        return HttpResponse(response_data,content_type = 'application/json',status=200)


    if request.method =="DELETE":
        product.delete()
        return HttpResponse(204)

    python_data = {
        'error':'only GET, PUT, PATCH, and DELETE method is alowed'
    }
    response_data = json.dumps(python_data)
    return HttpResponse(request_data,content_type='application/json',status=405)


    