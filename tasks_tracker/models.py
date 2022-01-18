from django.db import models

#import django built-in User model
from django.contrib.auth.models import User

class Task(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # if user is deleted, item will be deleted too.
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["complete"]

    def __str__(self):
        return self.title

    
        
