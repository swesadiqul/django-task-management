from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import random
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            email = form.cleaned_data.get('email')
            random_num = random.randrange(5000, 10000)

            request.session['email'] = email
            request.session['otp'] = random_num

            subject = "Verification Code for Your Account"
            email = form.cleaned_data['email']
            body = f"""
            Dear [User],
            Your One-Time Password (OTP) for accessing your account is: {random_num}

            This OTP is valid for 10 minutes. Please do not share this code with anyone.

            If you did not request this OTP, please contact our support team immediately.

            Thank you,
            [Your Company Name]
            """

            DEFAULT_FROM_EMAIL = 'support@psdcedu.xyz'

            send_mail(
                subject,
                body,
                DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
        else:
            print(form.errors)
            return JsonResponse({'message': 'Invalid form data.'})
        
    return JsonResponse({'message': 'Invalid Form.'})


def verify_account(request):
    user_otp = int(request.POST.get('otp'))
    session_otp = request.session.get('otp')

    if user_otp == session_otp:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
    else:
        messages.error(request, 'Invalid OTP.')

    return redirect('home')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            
        else:
            messages.error('Invalid username or password.')

    return redirect('home')


def signout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('/')