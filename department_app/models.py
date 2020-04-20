from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    amount = models.CharField(max_length=6)
    balance = models.CharField(max_length=6)
    total = models.CharField(max_length=6)
    mobile = models.CharField(max_length=15)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.fullname)