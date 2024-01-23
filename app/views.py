from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.core.mail import send_mail

from django.http import HttpResponse

def media(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo1':ufo,'pfo1':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('registration is successfull')
        else:
            return HttpResponse('invalid data')


    return render(request,'register.html',d)
