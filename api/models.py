
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('A','Architecture'),
        ('C','Client'),
    )
    user_role = models.CharField(choices=ROLE_CHOICES,max_length=2)



class ClientAccount(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Username = models.CharField(max_length=50)
    Number = models.IntegerField(null=True)
    Profile_pic = models.ImageField(upload_to='img',null=True,height_field=None, width_field=None, max_length=None)
    Email = models.EmailField(max_length=254,null=True)
    user = models.OneToOneField(User,verbose_name="User_id", on_delete=models.CASCADE)
    city = models.CharField(verbose_name="Location_City", max_length=50)
    date_time = models.DateTimeField( verbose_name="Created_at",auto_now=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.Username

class ArchitectureAccount(models.Model):
    Name = models.CharField(max_length=50,null=True)
    Username = models.CharField(max_length=50)
    Number = models.IntegerField(null=True)
    Profile_pic = models.ImageField(upload_to='img',null=True,height_field=None, width_field=None, max_length=None)
    Email = models.EmailField(max_length=254,null=True)
    user = models.OneToOneField(User,verbose_name="User_id", on_delete=models.CASCADE)
    Address = models.TextField(null=True)
    Reviews = models.IntegerField(null=True,default=0)
    city = models.CharField(verbose_name="Location_City", max_length=50)
    date_time = models.DateTimeField( verbose_name="Created_at",auto_now=True)


    def __str__(self):
        return self.Username

    
class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    posted_by=models.ForeignKey(ClientAccount, on_delete=models.CASCADE)
    createdAt=models.DateTimeField(auto_now=True)
    img=models.ImageField(upload_to='img/projects', height_field=None, width_field=None,null=True)
    apply_for = models.ManyToManyField(ArchitectureAccount,null=True)


    def __str__(self):
        return self.name

