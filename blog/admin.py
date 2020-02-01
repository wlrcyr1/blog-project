from django.contrib import admin
from blog.models import *
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Blog)
admin.site.register(UserFans)
admin.site.register(Category)
admin.site.register(ArticleDetail)
admin.site.register(UpDown)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Article2Tag)