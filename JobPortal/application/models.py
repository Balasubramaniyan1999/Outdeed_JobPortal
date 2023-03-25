from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    service = models.CharField(max_length=15,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Description(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    branch = models.CharField(max_length=50,null=False,blank=False)
    skills = models.CharField(max_length=200,null=False,blank=False)
    experience = models.CharField(max_length=50,null=False,blank=False)
    company_name = models.CharField(max_length=150,null=False,blank=False)
    openings = models.IntegerField(null=False,blank=False)


    def __str__(self):
        return self.name