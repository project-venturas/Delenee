from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .functions import handle_message, handle_status
import json

@csrf_exempt 
def whatsappWebhook(request):
    if request.method == "GET":
        VERIFY_TOKEN = "8811b434-baf7-4e1f-ae75-8f672229cb0b"
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse("Error, wrong validation token", status=400)
    
    elif request.method == "POST":
        data=json.loads(request.body)
        print("whatsappWebhook>>>", data)
        response_value = data['entry'][0]['changes'][0]['value']
        if 'messages' in response_value:
            handle_message(response_value['messages'])
        
        if 'statuses' in response_value:
            handle_status(response_value['statuses'][0]['status'], response_value['statuses'][0]['recipient_id'])

        
        return HttpResponse("Success", status=200)
    else:   
        return HttpResponse("Error", status=400)