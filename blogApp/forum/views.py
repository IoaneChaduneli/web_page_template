from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 
                'home.html',
                context={
                    'name': request.GET.get('q', '').title
                })

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request,
                 'login.html',
                 context={
                    'name': request.GET.get('loggin', '')
                 })
                

                            
