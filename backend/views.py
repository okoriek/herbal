from django.shortcuts import render

def home(request):
    
    return render(request, 'backend/index.html')


def contact(request):

    return render(request, 'backend/contact.html')
