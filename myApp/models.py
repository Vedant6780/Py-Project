from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    feedback=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name