from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# class Profileadd(models.Model): 
class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    bio=models.CharField(max_length=20)
    time_line_pic=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)




class Social(models.Model):
    title=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=40)

    def _str_(self):
        return self.title