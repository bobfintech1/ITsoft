from uuid import uuid4

from django.db import models

# Create your models here.


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'it_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class ItAboutModels(models.Model):
    title = models.CharField('title', max_length=70)
    about = models.CharField('about', max_length=10000)
    about_image = models.ImageField('photo', null=True, blank=True)
    video = models.FileField(upload_to='video/%y', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

