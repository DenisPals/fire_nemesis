from django.shortcuts import render
from .helpers import *
import os, json

PHONE_NUMBER = '0330 223 7058'

# Create your views here.
def index(request):
    service_account_info = json.loads(os.environ['SERVICE_ACCOUNT_KEY'])
    print(f'CUSTOME MESSAGE: {service_account_info}')
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Call email API
        gmail_send_message(
            intent='sendMessageToDenis',
            subject=subject, 
            user_name=name, 
            user_email=email, 
            user_message=message
        )
        return render(request, 'fire/index.html', {'PHONE_NUMBER': PHONE_NUMBER, 'messageSent': True})

    return render(request, 'fire/index.html', {'PHONE_NUMBER': PHONE_NUMBER, 'messageSent': False})