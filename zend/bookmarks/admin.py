from django.contrib import admin
from bookmarks.models import Link,Bookmark,Tag
#class ChoiceInline(admin.StackedInline):

class LinkAdmin(admin.ModelAdmin):
    pass   
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','link','user')
    list_filter = ('user',)
    ordering = ('title',)
    search_fields = ('title',)
class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link,LinkAdmin)
admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Tag,TagAdmin)
# Register your models here.
