from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(null=True, blank=True,max_length=500)
    phonenumber=models.IntegerField()
    def __str__(self):
        return super().__str__()
    
    
    
    
