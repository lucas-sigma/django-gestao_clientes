from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
        
            cliente_username  = form.cleaned_data.get('username')
            cliente_password  = form.cleaned_data.get('password')

            # user = authenticate(username = cliente_username, password = cliente_password)

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})