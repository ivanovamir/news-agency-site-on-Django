from django.contrib import admin

from .models import *
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'post_time_created', 'is_published', 'views_count')
    list_display_links = ('id', 'author')
    search_fields = ('id', 'author')
    prepopulated_fields = {'slug':('title',)}

    def views_count(self, obj):
        return len(obj.ip.all())
    views_count.short_description = 'Views'


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'post_time_created')
    list_display_links = ('id', 'news')
    search_fields = ('id', 'news')


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('id','name')    


class IpsAdmin(admin.ModelAdmin):
    list_display = ('id','ip')
    list_display_links = ('id','ip')
    search_fields = ('id','ip') 


admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Ip, IpsAdmin)