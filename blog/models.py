from django.db import models
from datetime import datetime
# rich text from tinymce 
from tinymce import models as tinymce_models

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
    desc = tinymce_models.HTMLField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    # short title 
    def title50(self):
        if len(self.title) > 50:
            return self.title[0:50] + '...'
        else:
            return self.title

    # short descriptions 
    def desc150(self):
        if len(self.desc) > 150:
            return self.desc[0:150] + '...'
        else:
            return self.desc

