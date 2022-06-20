from django.shortcuts import render,HttpResponse
from datetime import datetime

from urllib3 import HTTPResponse
from home.models import Index
from django.contrib import messages
from django.db.models import Count


# Create your views here.
def index(request):
    if request.method == "POST" :
        if Index.objects.filter(name=request.POST.get('name'), email=request.POST.get('email')).count() < 2 :
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            acc=request.POST.get('acc')
            ifsc=request.POST.get('ifsc')
            desc=request.POST.get('desc')
            index=Index(name=name,email=email,phone=phone,acc=acc,ifsc=ifsc,desc=desc,date=datetime.today())
            index.save()
            messages.success(request, 'Your message has been sent!')

        else :
            messages.success(request, 'Your message has not been sent!')


    # if request.method == "POST":
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     phone=request.POST.get('phone')
    #     acc=request.POST.get('acc')
    #     ifsc=request.POST.get('ifsc')
    #     desc=request.POST.get('desc')
    #     index=Index(name=name,email=email,phone=phone,acc=acc,ifsc=ifsc,desc=desc,date=datetime.today())
    #     index.save()
    #     messages.success(request, 'Your message has been sent!')

    return render(request,'index.html')
    # return HttpResponse('this is homepage')