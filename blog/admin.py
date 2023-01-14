from django.contrib import admin
from .models import SocialLink, Tag, Post

class SocialLinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SocialLink._meta.get_fields()]
    fieldsets = [
        ('Site Information', {'fields': ['link_name','link_created_date']}),
        ('Link Url', {'fields': ['link_url'], 'classes': ['']}),
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields() if field.name != 'tags']
    fieldsets = [
        ('Post Information', {'fields': ['title','date_posted']}),
        ('Author', {'fields': ['author'], 'classes': ['']}),
        ('Image', {'fields': ['image']}),
        ('Content', {'fields': ['tags','content'], 'classes': ['']}),
    ]

admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)


#field.name for field in Post._meta.get_fields() if field.name != 'content'
