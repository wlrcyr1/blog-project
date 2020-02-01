# -*-coding:utf-8-*-
from django.contrib import admin
from blog.models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title', 'category', 'read_count', 'comment_count',)
    #list_display_links=('title','desc','click_count',)
    #list_editable=('click_count',)
    fieldsets= ((None, {'fields': ('title', 'category', 'summary','content',)}),
        ('高级设置', {'classes': ('collapse',), 'fields': ( 'read_count', 'comment_count',)}),
        )
    class Media:
        js=(
        '/static/bootstrap/js/kindeditor/kindeditor-all-min.js',
        '/static/bootstrap/js/kindeditor/lang/zh-CN.js',
        '/static/bootstrap/js/kindeditor/config.js',
        )


admin.site.register(UserInfo)
admin.site.register(UserFans)
admin.site.register(Category)
admin.site.register(UpDown)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Article2Tag)