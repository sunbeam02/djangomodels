from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm,SignUpForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import Profile
from core.models import Store

# Create your views here.

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                user = authenticate(email=email, password=password)

                if user is not None:
                    request.session['user_id'] = str(user.id)
                    return redirect('dashboard')
                else:
                    return render(request, 'accounts/login.html', {'form':form})
                
        except ValidationError as err:
            return render(request, 'accounts/login.html', {'form':form, 'error':err}) 
           
    else:

        form = LoginForm
        return render(request, 'accounts/login.html', {'form':form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = SignUpForm()
    return render(request, "accounts/signup.html",{'form':form})


def dashboard(request):
    user_id = request.session['user_id']
    user = Profile.objects.get(id=user_id)
    store = Store.objects.get(owner = user)
    return render(request, 'accounts/dashboard.html', {'store':user})

