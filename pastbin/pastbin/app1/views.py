import json
from .models import Link
from .serializers import ContentSerializer
from .code import generatecode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
# Create your views h

@csrf_exempt
def generate_link(request):
    if request.method=='POST':
        content = json.loads(request.body)

        serializer = ContentSerializer(data=content)

        if serializer.is_valid():
            code = generatecode()
            obj = Link.objects.create(content = serializer.validated_data['content'],code=code,expired_at=timezone.now() + timedelta(minutes=1))

            url = request.build_absolute_uri(f"/{code}/")
            return JsonResponse({"url":url},status=201)
        else:
            response_data = {"message":"Invalid content"}
            return JsonResponse(response_data,status = 400)

    response_data = {"message":"method not allowed"}

    return JsonResponse(response_data,status=405)

@csrf_exempt
def get_message(request,code):
    if request.method=='GET':
        message = Link.objects.get(code=code)
        if  message.expired_at and  timezone.now() > message.expired_at:
            response_data = {"Message":"This message has expired"}
        else: response_data = {"message":message.content}

        return JsonResponse(response_data,status=200)
    response_data = {"message":"Method not allowed"}

    return JsonResponse(response_data,status=405)


