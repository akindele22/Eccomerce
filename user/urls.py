#This is an url for our apps
from django.urls import path
from django.contrib.auth import views as auth_views
#from user import views as user_views
from user import views as user_views 

urlpatterns = [
    path('signUp/', user_views.signUp,name='signUp'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='user/logout.html'), name='logout'),
    path('sent/', user_views.activation_sent_view, name = 'sent'),
    path('activate/', user_views.activate, name= 'activate'),
]