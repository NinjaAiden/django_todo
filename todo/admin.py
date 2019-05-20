from django.contrib import admin
from .models import Item

# Register your models here.
# register database model "Item" in admin site
admin.site.register(Item)