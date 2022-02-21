from django.db import models


class crudModel(models.Model):
    
    name=models.CharField(max_length=30)
    date=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    deleted=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
# Create your models here.
