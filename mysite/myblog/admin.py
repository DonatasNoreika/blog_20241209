from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["author", 'title', 'created']

# Register your models here.
admin.site.register(Post, PostAdmin)