from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail

from store.settings import EMAIL_HOST_USER
from .import forms


# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('accounts:user-customer') # go to update customer
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # log in user in
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')  # go to home page
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('my-app:homepage')


@login_required(login_url="/accounts/signup")
def user_customer(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('my-app:homepage')
                # return HttpResponse("Success create user!")
            except Exception as e:
                print(e)
                return HttpResponse('user exisit in the list') 
    else:
        form = forms.UserForm()

    return render(request, 'accounts/user-customer.html', {'form': form})
    

# user details
@login_required(login_url="/accounts/login")
def user_details(request):
    if request.method == "POST":
        form = forms.CreateUserDetail(request.POST, request.FILES)
        if form.is_valid():
            # save to the data base
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('my-app:homepage') # go to home page
    else:
        form = forms.CreateUserDetail()
    return render(request, 'accounts/user-detail.html', {'form': form})


def forgot_password(request):
    if request.method == "POST":
        sub = forms.ForgotForm(request.POST)
        subject = "Wellcome to ambrsoft"
        message = "Hope are you enjoying"
        recepient = str(sub['email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        
        return render(request, 'accounts/success-password.html', {'recpinet': recepient})
    
    else:
        sub = forms.ForgotForm()

    return render(request, 'accounts/forgot-password.html', {'form': sub})
        