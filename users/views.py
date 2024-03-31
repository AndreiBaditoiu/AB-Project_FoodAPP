from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created')
            return redirect('food:index')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
# 'form.is_valid()' verifica username ( su nu fie duplicat).
