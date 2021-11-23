from django.shortcuts import render, redirect
from .forms import Register
from .models import Verification
import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = Register()
        if request.method == 'POST':
            form = Register(request.POST)
            if form.is_valid():
                new_user = form.save()
                uid = uuid.uuid4()
                verification_obj = Verification(user=new_user, token=uid)
                verification_obj.save()
                send_reg_email(new_user.email, uid)
                messages.success(
                    request, "Your Account Created! Please verify your account check your email")
                return redirect('/login')

    context = {'form': form}
    return render(request, 'register.html', context)


def send_reg_email(email, token):
    subject = 'Verify Email'
    message = f'Hello user! Click on the below link to verify your email http://127.0.0.1:8000/account-verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message,
              from_email=from_email, recipient_list=recipient_list)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            verify = Verification.objects.get(user=user)
            if verify.verify:
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def profile(request,username):
    user = User.objects.filter(username = username)[0]
    return render(request, 'profile.html',{'user':user})


def logoutUser(request):
    logout(request)
    return redirect('login')


def account_verify(request, token):
    pf = Verification.objects.filter(token=token).first()
    pf.verify = True
    pf.save()
    messages.success(
        request, "Your Account has been verified, Now you can login")
    return redirect('/login')

def editprofile(request):
    return render(request,'editprofile.html')