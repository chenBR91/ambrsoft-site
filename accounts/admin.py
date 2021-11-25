from django.contrib import admin

from . models import Customer, ForgotPassword

# Register your models here.


admin.site.register(Customer)
admin.site.register(ForgotPassword)