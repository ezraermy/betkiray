from django.contrib import admin
from .models import Renter, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Renter)