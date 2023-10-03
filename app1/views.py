from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, 'index.html')

def contact(request):
    
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
            email, 
            ['nasib4patel@gmail.com'], 
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent')

    
    return render(request, 'index.html')




