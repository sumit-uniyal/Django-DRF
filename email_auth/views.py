from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
from .utils import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .searilizers import *
from rest_framework import viewsets

# Create your views here.
def home(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        save_data = Mail(
            name= name,
            email=email,
            message=message
        )
        save_data.save()

        send_emails(name, message, email)             

    return render(request, 'email_auth/home.html')

def list(request):
    email_data = Mail.objects.all()

    return render(request, 'email_auth/list.html', context={'data':email_data})

def update_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data_id = request.POST.get('data_id')

        email_data = Mail.objects.get(pk=data_id)
        email_data.name = name
        email_data.email = email
        email_data.message = message
        email_data.save()
        
    email_data = Mail.objects.all()

    return render(request, 'email_auth/list.html', context={'data':email_data})

@api_view(['GET'])
def index(request):
    test={
        's':'sum',
        'k':'aus'
    }
    return Response(test)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def mail_sea(request):
    if request.method == 'GET':
        objs = Mail.objects.all()
        serializers = Mail_searilizer(objs, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        data = request.data
        serializers = Mail_searilizer(data = data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Mail.objects.get(id = data['id'])
        serializers = Mail_searilizer(obj, data = data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Mail.objects.get(id = data['id'])
        serializers = Mail_searilizer(obj, data = data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    else:
        data = request.data
        obj = Mail.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person data is deleted'})
    
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = request.data
        serializers = login_serilizer(data = data)
        if serializers.is_valid():
            data = serializers.data
            return Response ({'message': 'Success'})
        return Response (serializers.errors)
    
class sumit(viewsets.ModelViewSet):
    serializer_class = Mail_searilizer
    queryset = Mail.objects.all()