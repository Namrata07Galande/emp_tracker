from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class employee(models.Model):
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    age =models.IntegerField()
    gender = models.CharField(max_length=50)
    company_name = models.CharField(max_length=60)
    department_name = models.CharField(max_length=100)
    leave_available = models.IntegerField()

class holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)

class emp_leave(models.Model):
    startdate = models.DateField("startdate (yyyy-mm-dd)", auto_now_add=False, auto_now=False, blank=True, null=True)
    enddate = models.DateField("enddate (yyyy-mm-dd)", auto_now_add=False, auto_now=False, blank=True, null=True)
    reason = models.CharField(max_length=500)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)