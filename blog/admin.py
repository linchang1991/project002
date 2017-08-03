from django.contrib import admin
from .models import Blog, Tag, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')

class TagAdmin(admin.ModelAdmin):
	list_display = ('name',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('content',)

		

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

