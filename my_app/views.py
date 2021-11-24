from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


def homepage(request):
    # return HttpResponse("Hello chen")
    all_users = User.objects.all()
    print()
    return render(request, 'app/homepage.html', {'users': all_users})
    

