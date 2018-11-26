from django.urls import path
from . views import home,login_user,logout_user,register_user,edit_profile,change_password

urlpatterns = [
    path('',home,name='home'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_user,name='register'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    path('change_password/',change_password,name='change_password')
]
