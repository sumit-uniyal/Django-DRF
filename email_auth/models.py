from django.db import models

# Create your models here.
class Color(models.Model):
    color_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.color_name
    
class Mail(models.Model):
    color = models.ForeignKey(Color, null= True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length= 50)
    message = models.TextField()

    def __str__(self):
        return self.name
    
