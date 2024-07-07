from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True,null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):

        return self.username

class Uploader(models.Model):
    from library.models import Faculty,Department
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    profile_pic = models.ImageField(upload_to = "profile_pics")
    def __str__(self):

        return f"{self.user.username}"
