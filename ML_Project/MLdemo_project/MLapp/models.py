from django.db import models


class Programming(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    programming=models.ForeignKey(Programming,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class order(models.Model):
    Name=models.CharField(max_length=100)
    DOB=models.DateField(max_length=10)
    Age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phono=models.IntegerField()
    email=models.EmailField(max_length=40)
    address=models.TextField(max_length=250)
    departmentname=models.ForeignKey(Programming,on_delete=models.SET_NULL, blank=True, null=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL, blank=True,null=True)
    purpose=models.CharField(max_length=100)
    materials=models.CharField(max_length=40)
    def __str__(self):
        return self.Name