from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'ip'
        ordering = ['-id']


class News(models.Model):
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField(null=False)
    photo = models.ImageField(null=True, upload_to = "new/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    post_time_created = models.DateTimeField(auto_now_add=True, null=False)
    tags = models.ForeignKey('Tag', on_delete=models.CASCADE)
    views = models.ManyToManyField(Ip, related_name = 'post_views', blank=True)

    def __str__(self):
        return f"{self.title}, {self.author}"

    def get_absolute_url(self):
        return reverse ('show_new', kwargs ={'slug_new': self.slug})

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'list of new'
        # verbose_name_plural = 
        ordering = ['-post_time_created']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse ('show_tag', kwargs ={'slug_tag': self.name})

    class Meta:
        verbose_name = 'Tag'
        ordering = ['id']

class Review(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    post_time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.body

    # def get_absolute_url(self): 
    #     return reverse ('show_new', kwargs ={'slug_new': self.book})

    class Meta:
        verbose_name = 'Review'
        ordering = ['post_time_created']