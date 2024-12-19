from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_page')  # Redirect ไปที่ chat_page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def chat_page(request):
    return render(request, 'chat.html')  # โหลดเทมเพลต chat.html
