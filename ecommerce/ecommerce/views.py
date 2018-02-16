from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import NameForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate , login,get_user_model

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
 
def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated())
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect('/login')
        else:
            print('Error')

    return render(request,"auth/login.html",context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user =  User.objects.create_user(username,email,password)
    return render(request,"auth/register.html",context)



