from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

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
