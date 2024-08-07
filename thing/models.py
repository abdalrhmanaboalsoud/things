from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Thing(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    number = models.IntegerField()
    size = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name