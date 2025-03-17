from django.db import models
class cienima(models.Model):
    name= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image= models.ImageField(upload_to='cienima/')
    description = models.TextField()
    def __str__(self):
        return self.name
