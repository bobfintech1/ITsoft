from uuid import uuid4

from django.db import models


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'it_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class ItMainBlogs(models.Model):
    header = models.CharField('title', max_length=50)
    header_image = models.ImageField(upload_to= upload_location, null=True, blank=True)
class ItAboutBlogs(models.Model):
    about = models.CharField('about', max_length=20)
    about_body = models.TextField()
    about_image = models.ImageField(upload_to= upload_location, null=True, blank=True)
class ItServiceBlogs(models.Model):
    services = models.CharField('title', max_length=30)
    services_body = models.TextField('body',)
    services_image1 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    services_image2 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    services_image3 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    services_image4 = models.ImageField(upload_to=upload_location, null=True, blank=True)
class ItBlogBlogs(models.Model):
    blog_title = models.CharField('blog', max_length=15)
    blog_image1 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    blog_image2 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    blog_image3 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    blog_image4 = models.ImageField(upload_to=upload_location, null=True, blank=True)
class ItPartnersBlogs(models.Model):
    partners_title = models.CharField('partners', max_length=15)
    partners_logo1 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo2 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo3 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo4 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo5 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo6 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo7 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo8 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo9 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo10 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo11 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo12 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo13 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo14 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo15 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo16 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo17 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo18 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo19 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo20 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    partners_logo21 = models.ImageField(upload_to=upload_location, null=True, blank=True)


    def __str__(self):
        return str(self.header)