from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests, json


def webhook(request):
    dispatch(request)
    print(request)
    fb_receive_message(request)
    '''
    incoming_message = json.loads(request.body)
    print(incoming_message)



    incoming_message = requests.get(request)
    print(incoming_message)
    for entry in incoming_message['entry']:
        for message in entry['messaging']:
            if 'message' in message:
                print(message)
'''
    verify_code = 'webhook'
    verify_token = request.GET.get('hub.verify_token')
    if verify_code == verify_token:
        return HttpResponse(request.GET.get('hub.challenge'))
    else:
        return HttpResponse('False')


def dispatch(self, request, *args, **kwargs):
    return dispatch(self, request, *args, **kwargs)


def fb_receive_message(request):
    message_entries = json.loads(request)['entry']
    for entry in message_entries:
        messagings = entry['messaging']
        for message in messagings:
            sender = message['sender']['id']
            if message.get('message'):
                text = message['message']['text']
                print("{} says {}".format(sender, text))
    return "Hi"


# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
