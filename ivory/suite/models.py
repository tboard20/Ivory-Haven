from django.db import models

# Create your models here.



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message= models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    note = models.TextField(blank=True, null=True)
    date_in = models.CharField(max_length=50)
    date_out = models.CharField(max_length=50)
    adult = models.CharField(max_length=5,blank=True, null=True)
    child = models.CharField(max_length=5,blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"