# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # from django.contrib.auth import get_user_model
# from .manager import UserManager

# # user = get_user_model()

# # Create your models here.

# class Customuser(AbstractUser):

#     username=None
#     # fname = models.CharField(max_length=20)
#     # lname = models.CharField(max_length=20)
#     phone_number = models.CharField(max_length=15, unique=True)
#     email= models.EmailField(unique=True)
#     user_bio = models.CharField(max_length=50)
#     profile_pic = models.ImageField(upload_to="profile")
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
    
    
    

#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = ["email"]
#     objects = UserManager()

