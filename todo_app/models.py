from django.db import models
from django.contrib.auth.models import User

#  Create your models here.
class tasklists(models.Model):
    manage=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=50)
    done=models.BooleanField(default=True)
    
    def __str__(self):
        return self.task
    