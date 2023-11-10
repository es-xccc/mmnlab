from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def redhom(request):
    return redirect('polls/login')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('polls/login_success')
        else:
            return render(request, 'polls/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'polls/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'polls/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'polls/register.html', {'form': form})

def login_success(request):
    return render(request, 'polls/login_success.html')

def logout_view(request):
    logout(request)
    return redirect('polls/login')