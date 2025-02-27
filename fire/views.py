from django.shortcuts import render

PHONE_NUMBER = '0330 223 7058'

# Create your views here.
def index(request):
    return render(request, 'fire/index.html', {'PHONE_NUMBER': PHONE_NUMBER})