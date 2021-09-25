from django.contrib import admin
from .models import Post, Tags
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title' ,'autor')}
    list_display =('title','autor','criacao')

admin.site.register(Post, PostAdmin)
admin.site.register(Tags)