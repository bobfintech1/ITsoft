# Generated by Django 3.2.13 on 2022-05-12 19:26

import IT_blogs.blogs.mainpage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_blogs', '0014_mainpageaboutmodel_mainpageblogmodel_mainpageheadermodel_mainpagenumbersmodel_mainpageservicemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpageblogmodel',
            name='body',
        ),
        migrations.AlterField(
            model_name='mainpageblogmodel',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageblogmodel',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageblogmodel',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageblogmodel',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageheadermodel',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageheadermodel',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageheadermodel',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageservicemodel',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageservicemodel',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageservicemodel',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
        migrations.AlterField(
            model_name='mainpageservicemodel',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=IT_blogs.blogs.mainpage.upload_location),
        ),
    ]