from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=55, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='mymedia', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title



# Create your models here.
