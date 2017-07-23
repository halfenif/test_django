from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True, null=True)
    url = models.URLField('URL', unique=True)
    desc=models.CharField('DESC', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
