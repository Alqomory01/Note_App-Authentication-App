from django.contrib import admin
from .models import *

class Noteadmin(admin.ModelAdmin):
    title =['id', 'title', 'created_at']
    content = ['id', 'content', 'created_at']
    image = ['id', 'image', 'created_at']
    
    


admin.site.register(Note, Noteadmin)

# Register your models here.
