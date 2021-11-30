from django.db import models
from datetime import datetime

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class subCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self):
        return self.name

class blogPost(models.Model):
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True )
    subCategory = models.ForeignKey(subCategory, on_delete=models.SET_NULL, null=True, blank=True )
    date = models.DateField(default=datetime.now)
    title = models.CharField(max_length=500)
    desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

