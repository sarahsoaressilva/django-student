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
    show = models.BooleanField(default=True) 
    picture = models.ImageField(blank=True, upload_to='pictures/%Y_%M') # Pictures depende do Pillow
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Return the concatenation of the first name and last name.
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


