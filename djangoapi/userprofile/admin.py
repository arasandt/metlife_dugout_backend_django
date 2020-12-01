from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileadmin(admin.ModelAdmin):
    list_display = ['id','firstName','lastName', 'email', 'coins', 'rank']
