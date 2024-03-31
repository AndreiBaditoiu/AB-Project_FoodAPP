from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# 'form.is_valid()' verifica username ( su nu fie duplicat).


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
