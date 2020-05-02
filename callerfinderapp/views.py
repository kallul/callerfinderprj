from django.shortcuts import render
from django.http import HttpResponse

from .models import Truecaller
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json
import urllib.parse
import os


def index(request):
    return render(request, 'callerfinderapp/index.html')
    
def get_name(access_token):
    url = 'https://profile4.truecaller.com/v1/default'
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + access_token}
    r = requests.get(url, headers=headers)
    json_data = json.loads(r.text)

    return json_data['name']['first'] + ' ' + json_data['name']['last']


def ajaxpost(request):
    phone_number = request.POST['phone_number']

    url = 'https://api4.truecaller.com/v1/apps/requests'
    headers = {'content-type': 'application/json', 'appKey': '4rzuQf498e7305d4f443d8545514dc48fa3af'}
    data = {'phoneNumber': phone_number}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    json_data = json.loads(r.text)
    truecaller_model = Truecaller()
    truecaller_model.requestId = json_data['requestId']
    truecaller_model.phone_number = phone_number
    truecaller_model.save()
    return JsonResponse({
        'status_code': r.status_code,
        'text': r.text,
        'requestId': json_data['requestId']})


@csrf_exempt
def truecaller(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode(encoding='UTF-8'))
            truecaller_model = Truecaller.objects.filter(requestId=json_data['requestId']).get()
            truecaller_model.access_token = json_data['accessToken']
            truecaller_model.save()
            return JsonResponse({'message': 'Success'})
        except:
            return JsonResponse({'message': 'Invalid request', 'status': 'FAILED'})
    else:
        try:
            requestId = urllib.parse.unquote(request.GET['requestId'])
            truecaller_model = Truecaller.objects.filter(requestId=requestId).get()
            if truecaller_model.access_token:
                return JsonResponse({'message': 'Success', 'status': 'OK', 'name': get_name(truecaller_model.access_token)})
            else:
                return JsonResponse({'message': 'Failed', 'status': 'NO'})
        except:
            return JsonResponse({'message': 'Invalid request', 'status': 'FAILED'})
