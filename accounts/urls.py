from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user-details/', views.user_details, name='user-details'),
    path('user-customer/', views.user_customer, name='user-customer'),
    path('reset/', views.forgot_password, name='forgot-password'),
]