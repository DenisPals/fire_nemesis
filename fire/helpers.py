"""Gmail API Dependencies"""
from google.oauth2 import service_account
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError
import google.auth  
import json, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse



def gmail_send_message(**kwargs):

        """Gmail API"""
        # Following kwargs required
        # intent, subject, gmail_email, message_content, recipient

        # SERVICE_ACCOUNT_FILE = 'fire_nemesis_mailService'
        # credentials = service_account.Credentials.from_service_account_file(
        #     filename=SERVICE_ACCOUNT_FILE,
        #     scopes=['https://mail.google.com/'],
        #     subject='noreply@fire-nemesis.com'
        # )

        service_account_info = json.loads(os.environ['SERVICE_ACCOUNT_KEY'])
        credentials = service_account.Credentials.from_service_account_info(service_account_info)

        if kwargs['intent'] == 'sendMessageToDenis':
          
          try:
              service = build('gmail', 'v1', credentials=credentials)
              message = EmailMessage()

              message['To'] = 'denis@fire-nemesis.com'
              message['From'] = 'noreply@fire-nemesis.com'
              message['Subject'] = 'Support request Fire Nemesis'
              message['List-Unsubscribe'] = '<https://www.fire-nemesis.com/unsubscribe>'
              message['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'

              content = f'''
Support request received
From: {kwargs['user_email']}
Name: {kwargs['user_name']}
Subject: {kwargs['subject']}
Message: {kwargs['user_message']}'''
              message.set_content(content)

              # encoded message
              encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                  .decode()

              create_message = {
                  'raw': encoded_message
              }
              # pylint: disable=E1101
              send_message = (service.users().messages().send(userId="me", body=create_message).execute())
              message_id = send_message['id']
              print(F'Message Id: {message_id}')

          except HttpError as error:
              print(F'An error occurred: {error}')
              send_message = None

          gmail_send_message(
              intent='automaticMessageReply', 
              subject=kwargs['subject'], 
              user_name=kwargs['user_name'], 
              user_email=kwargs['user_email']
              )
          return True  #JsonResponse(send_message, safe=False)
        
        if kwargs['intent'] == 'automaticMessageReply':
          try:
              service = build('gmail', 'v1', credentials=credentials)
              message = EmailMessage()

              message = MIMEMultipart('alternative')
              message['To'] = kwargs['user_email']
              message['From'] = 'noreply@fire-nemesis.com'
              message['Subject'] = kwargs['subject']

              file_name = 'fire/templates/fire/emailTemplate_0.html'
              file = open(file_name, 'r', encoding='utf-8')

              content = file.read()
              file.close()
              message.attach(MIMEText(content, 'html'))

              # encoded message
              encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                  .decode()

              create_message = {
                  'raw': encoded_message
              }
              # pylint: disable=E1101
              send_message = (service.users().messages().send(userId="me", body=create_message).execute())
              message_id = send_message['id']
              print(F'Message Id: {message_id}')

          except HttpError as error:
              print(F'An error occurred: {error}')
              send_message = None

          return True  #JsonResponse(send_message, safe=False)
        