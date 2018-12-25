from django.contrib import admin
from .models import Homepage
from .models import Post
from .models import Comment

admin.site.register(Homepage)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)