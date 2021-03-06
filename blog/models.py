# -*- coding:utf-8 -*-
from django.db import models


class UserInfo(models.Model):
    """
    用户表
    """
    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)
    nickname = models.CharField(verbose_name='昵称', max_length=32, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', unique=True, null=True, blank=True)
    avatar = models.ImageField(verbose_name='头像', null=True, blank=True, upload_to='avatar')

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    fans = models.ManyToManyField(verbose_name='粉丝们',
                                  to='UserInfo',
                                  through='UserFans',
                                  related_name='f',
                                  through_fields=('user', 'follower'))

    '''print的时候显示'''
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户表'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-nid']



class UserFans(models.Model):
    """
    互粉关系表
    """
    user = models.ForeignKey(verbose_name='博主', to='UserInfo', to_field='nid',
                             on_delete=models.CASCADE,
                             related_name='users')
    follower = models.ForeignKey(verbose_name='粉丝',to='UserInfo', to_field='nid',
                                 on_delete=models.CASCADE,
                                 related_name='followers')

    # 联合唯一
    class Meta:
        verbose_name = '互粉关系表'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-id']
        unique_together = [
            ('user', 'follower'),
        ]


class Category(models.Model):
    """
    文章分类表
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=128)
    index = models.IntegerField(verbose_name='分类排序', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章分类表'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-nid']


class UpDown(models.Model):
    """
    文章顶或踩
    """
    article = models.ForeignKey(verbose_name='文章', to='Article', to_field='nid', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='赞或踩用户', to='UserInfo', to_field='nid', on_delete=models.CASCADE)
    up = models.BooleanField(verbose_name='是否赞')

    class Meta:
        verbose_name = '文章顶或踩'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-id']
        unique_together = [
            ('article', 'user'),
        ]

class Comment(models.Model):
    """
    评论表
    """
    nid = models.BigAutoField(primary_key=True)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回复评论', to='self', related_name='back', null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(verbose_name='评论文章', to='Article', to_field='nid', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', to_field='nid', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论表'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-nid']

class Tag(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标签名称', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标签'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-nid']


class Article(models.Model):
    nid = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', max_length=128)
    content = models.TextField(verbose_name='文章内容', blank=True, null=True)
    summary = models.CharField(verbose_name='文章简介', max_length=255)
    read_count = models.IntegerField(verbose_name='阅读次数', default=0)
    comment_count = models.IntegerField(verbose_name='评论次数', default=0)
    #up_count = models.IntegerField(default=0)
    #down_count = models.IntegerField(default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    category = models.ForeignKey(verbose_name='文章类型', to='Category', to_field='nid',
                                 null=True, on_delete=models.CASCADE)

    type_choices = [
        (1, "Python"),
        (2, "Linux"),
        (3, "OpenStack"),
        (4, "GoLang"),
    ]
    article_type_id = models.IntegerField(choices=type_choices, default=None)

    tags = models.ManyToManyField(
        to="Tag",
        through='Article2Tag',
        through_fields=('article', 'tag'),
    )

    class Meta:
        verbose_name = '文章'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        ordering = ['-nid']


class Article2Tag(models.Model):
    article = models.ForeignKey(verbose_name='文章', to="Article", to_field='nid', on_delete=models.CASCADE)
    tag = models.ForeignKey(verbose_name='标签', to="Tag", to_field='nid', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '第二标签'  # 这个让后台显示我们自定的表名
        verbose_name_plural = verbose_name  # 因为是外国人设计的，如果不写这个会在名字后面跟一个s
        unique_together = [
            ('article', 'tag'),
        ]

