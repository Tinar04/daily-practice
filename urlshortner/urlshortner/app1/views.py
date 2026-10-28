from django.shortcuts import render,redirect
import json
from .serializers import ShortenSerializer
from .models import Links
from .code import generatecode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def generateUrl(request):
    if request.method=='POST':
        url = json.loads(request.body)

        serializer = ShortenSerializer(data=url)

        if serializer.is_valid():
            code = generatecode()
            Links.objects.create(original_url=serializer.validated_data['original_url'],code=code)
            shorten_url = request.build_absolute_uri(f"/{code}/")
            return JsonResponse({"shorten url":shorten_url},status=201)
        else:
            response_data = {"message":"Invalid url"}
            return JsonResponse(response_data,status=400)

    response_data = {"message":"Method not allowed"}

    return JsonResponse(response_data,status=405)

def redirect_to_og  (request,code):
    if request.method == 'GET':

        obj = Links.objects.get(code=code)
        obj.clicks+=1
        obj.save()

        return redirect(obj.original_url)

        



