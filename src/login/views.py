from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def log(request):  
    if request.user.is_authenticated:
        return redirect('/barmas/')
    else:
        if request.method == 'POST':
            user_name = request.POST.get('username')
            password1 = request.POST.get('password')
            
            User = authenticate(request, username=user_name, password=password1) 
            if User is not None:
                login(request, User)
                return redirect('barmas:tabel')
                
        return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')
    