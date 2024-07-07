from django.db import models
from accounts.models import User
# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):

        return f"{self.name}"
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "faculties"
    def __str__(self):

        return f"{self.name}"


class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty,related_name = "departments", on_delete= models.CASCADE)
    def __str__(self):

        return f"{self.name}"
class Course(models.Model):
    level = models.ForeignKey(Level,related_name="courses",on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    credit_unit = models.CharField(max_length=2)
    outline = models.TextField(max_length=300)
    department = models.ForeignKey(Department,related_name="courses",on_delete= models.CASCADE)
    faculty = models.ForeignKey(Faculty,related_name="courses",on_delete=models.CASCADE)
    def __str__(self):

        return f"{self.code}"
class Material(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to = "documents")
    course = models.ForeignKey(Course,related_name= "materials",on_delete= models.CASCADE)
    preview = models.TextField(max_length=100)
    def __str__(self):

        return f"{self.name}"
class Review(models.Model):
    material = models.ForeignKey(Material,related_name="reviews",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="reviews",on_delete=models.CASCADE)
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.user.username
