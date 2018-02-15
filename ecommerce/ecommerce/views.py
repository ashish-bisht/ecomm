from django.http import HttpResponse
from django.shortcuts import render
from .forms import NameForm

def home_page(request):
    context = {
        'title' : 'Ecommerce'
    }
    return render(request,"home_page.html",context)

def contact_page(request):
    contact_form =  NameForm(request.POST or None)
    context = {
        'title':'Contact us',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,"contact_page.html",context)

def about_page(request):
    
    return render(request,"about_page.html",context)
 