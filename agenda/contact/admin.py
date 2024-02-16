from django.contrib import admin
from contact import models

# Register your models here.

'''
Configuração da área de ADMIN 
'''
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name","last_name",
        "email", "phone", "created_date",
    )
    ordering = 'first_name',
    list_filter = 'created_date',
    search_fields = 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    # list_editable = 'phone',
    
