from django.db import models

# Create your models here.
class Item(models.Model):
    # create a name field with a limit of 30 characters, not allowed to be empty
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.name
