from django.db import models
class Service(models.Model):
    title = models.CharField('title', max_length=255)
    tagline = models.CharField('tagline', max_length=500)
    icon = models.CharField('icon', max_length=255)
    def __str__(self):
        return self.title