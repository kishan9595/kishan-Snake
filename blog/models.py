from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()
    img = models.ImageField(upload_to='images/', null=True, blank=True, )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 

    def save(self, *args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

def slugify_title(instance, save=False):
    
    slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{qs.count() + 1}"

    instance.slug = slug
    if save:
        instance.save()
    return instance

def article_pre_save(sender, instance, *args,**kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args,**kwargs):
    print('post_save')
    if created:
        slugify_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)

class Review(models.Model):
    VOTE_TYPE = {
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    }
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
