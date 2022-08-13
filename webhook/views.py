# webhook/views.py
# ...
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        return HttpResponse("Webhook received - 1!")