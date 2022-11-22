from django.db import models

class Menu(models.Model):
    name= models.CharField(max_length= 100)
    price= models.CharField(max_length = 100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.description}"
