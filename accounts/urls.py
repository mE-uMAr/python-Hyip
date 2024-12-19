from django.urls import path
from invest import views

urlpatterns = [
    path('login/' , views.login_user , name='login_user' )
]