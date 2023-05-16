from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def email(request):
    UO=Userform()
    SO=Studentform()
    d={'UO':UO,'SO':SO}
    if request.method=='POST' and request.FILES:
        ufo=Userform(request.POST)
        sfo=Studentform(request.POST,request.FILES)
        if ufo.is_valid() and sfo.is_valid():
            nufo=ufo.save(commit=False)
            pw=ufo.cleaned_data['password']
            nufo.set_password(pw)
            nufo.save()

            nsfo=sfo.save(commit=False)
            nsfo.username=nufo
            nsfo.save()

            send_mail('email',
            'demo registration is done',
            'bhushanroyal123@gmail.com',
            [nufo.email],
            fail_silently=False          
            )
            return HttpResponse('data inserted')
        else:
            return HttpResponse('invalid data ')
    return render(request,'email.html',d)