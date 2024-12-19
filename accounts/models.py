from django.db import models
from django.contrib.auth.models import AbstractUser 
from .manager import UserManager

class Customuser(AbstractUser):
    username = None
    p_number = models.CharField(max_length=11 ,unique=True)
    email = models.EmailField(blank=True)
    profile_img = models.ImageField(upload_to='profile-img' , blank=True , null=True)

    USERNAME_FIELD = 'p_number'
    REQUIRED_FIELDS=[]
    objects = UserManager()