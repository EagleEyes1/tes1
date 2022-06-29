from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def log(request):  
    if request.user.is_authenticated:
        return redirect('/barmas/')
    else:
        if request.method == 'POST':
            user_name = request.POST.get('username')
            password1 = request.POST.get('password')
            
            User1 = authenticate(request, username=user_name, password=password1) 
            if User1 is not None:
                login(request, User1)
                return redirect('barmas:tabel')
            else:
               messages.info(request, 'Username atau Password Salah')
               return redirect('login:login')

        return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')
    