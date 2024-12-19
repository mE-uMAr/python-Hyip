from django.urls import path
from . import views

urlpatterns = [
    path('deposit/' , views.deposit , name='deposit'),
    path('withdraw/' , views.withdraw , name = 'withdraw'),
    path('pay/<int:deposit_id>/' , views.pay , name='pay')
]