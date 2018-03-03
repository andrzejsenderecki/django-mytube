from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import Register
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
    else:
        register_form = Register()
    return render(request, 'register.html', {'register_form': register_form})

@login_required
def dashboard(request):
    user_name = User.objects.get(username=request.user)
    return render(request, 'dashboard.html', {'user_name': user_name})
