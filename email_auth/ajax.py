from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def get_data(request):
    
    id = request.POST.get('id')
    email_data = Mail.objects.get(pk = id)
    response_data = {
        'id': email_data.id,
        'name': email_data.name,
        'email': email_data.email,
        'message': email_data.message,
    }
    return JsonResponse(response_data)

def delete_data(request):
    id = request.POST.get('id')

    delete = Mail.objects.filter(pk=id).delete()

    if delete:
        response_data = {'message': 'Record deleted successfully.'}
    else:
        response_data = {'message': 'Record not found.'}

    return JsonResponse(response_data)