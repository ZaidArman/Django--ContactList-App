from django.db import models

# Create your models here.

class ContactlistModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    
    def to_string(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.comment