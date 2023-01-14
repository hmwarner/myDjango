from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]
    fieldsets = [
        ('User Information', {'fields': ['user','profile_created']}),
        ('About', {'fields': ['about_me'], 'classes': ['']}),
        ('Date of birth', {'fields': ['dob'], 'classes': ['']}),
        ('Avatar', {'fields': ['image'], 'classes': ['']}),
    ]

admin.site.register(Profile, ProfileAdmin)
