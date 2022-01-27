import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Inquiry(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text[:50] + '...'

class Alternative(models.Model):
    
    def __str__(self):
        return self.text[:50] + '...'