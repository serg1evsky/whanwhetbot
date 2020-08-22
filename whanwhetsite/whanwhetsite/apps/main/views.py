from django.shortcuts import render
from main.forms import UploadFileForm
from django.conf import settings 
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def index(request):
    if request.method == 'POST':
        now = os.getcwd()
        os.chdir(settings.FILES_ROOT)
        with open('settings.py', 'wb+') as destination:
            for chunk in request.FILES['settings.py'].chunks():
                destination.write(chunk)
        os.chdir(now)
        return render(request,'main/main.html')
    else:
        return render(request,'main/main.html')
    
        

