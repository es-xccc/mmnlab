from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def redhom(request):
    return redirect('learn/home')

def home(request):
    return render(request, 'learn/home.html')

def st_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('iblearning')
        else:
            return render(request, 'learn/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'learn/login.html')

def st_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'learn/st_register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'learn/st_register.html', {'form': form})

def monitor(request):
    return render(request, 'learn/monitor.html')

def ib_learning(request):
    return render(request, 'learn/ib_learning.html')

def logout_view(request):
    logout(request)
    return redirect('learn/st_login')