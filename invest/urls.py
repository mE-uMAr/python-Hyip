from django.urls import path , include
from . import views
from referal.views import *

urlpatterns = [
    path('' , views.home , name='home'),
    path('profile/' , views.profile , name = 'profile'),
    path('invite/' , invite , name = 'invite'),
    path('account/' , views.account , name = 'account'),
    path('signup/' , views.signup_user , name = 'signup'),
    path('signup/<str:ref_code>/' , views.signup_user , name='signup'),
    path('logout/' , views.logout_user , name = 'logout'),
    path('invest/' , views.invest , name = 'invest')
]