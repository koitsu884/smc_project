from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    title_ja = models.CharField(max_length=100, blank=True)
    title_ko = models.CharField(max_length=100, blank=True)
    title_zh = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    description_ja = models.TextField(blank=True)
    description_ko = models.TextField(blank=True)
    description_zh = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/services/')
    display_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title
