from django.db import models
from datetime import datetime


class Receiver(models.Model):
    """
    Class for company that receives the invoice
    """
    name = models.CharField(max_length=200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created = models.DateTimeField(default=datetime.now)
    
    # add later:
    # logo
    
    def __str__(self):
        return str(self.name)
    
