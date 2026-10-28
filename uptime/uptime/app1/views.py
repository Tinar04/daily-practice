from django.shortcuts import render
import json
from django.http import JsonResponse
from .serializers import LinkSerializer
from.test_check import check
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def checker(request):
    if request.method == 'POST':
        url = json.loads(request.body)


        serializer = LinkSerializer(data=url)

        if serializer.is_valid():
            result = check(serializer.validated_data['url'])

            response_data = {"Result":result}

            return JsonResponse(response_data,status=200)
    response_data = {"message":"method not allowed"}

    return JsonResponse(response_data,status=405)

    


