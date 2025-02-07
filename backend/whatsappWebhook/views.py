from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
        return HttpResponse("Success", status=200)
    else:
        return HttpResponse("Error", status=400)