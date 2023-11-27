from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    # id (primary_key, criado automaticamente)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # show = models.BooleanField(default=True)
    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # picture 

    def __str__(self):
        return self.frist_name + ' ' + self.last_name

