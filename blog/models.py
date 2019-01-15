from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content =  models.TextField() #Unrestricted text
    date_posted = models.DateTimeField(default = timezone.now) #current date time as created and changable
    author  = models.ForeignKey(User,on_delete=models.CASCADE) #telling that if a user is deleted then delete the user 

    def __str__(self):
        return self.title
    
    
