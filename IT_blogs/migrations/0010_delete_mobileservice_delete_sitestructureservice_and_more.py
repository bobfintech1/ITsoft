# Generated by Django 4.0.4 on 2022-05-13 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_blogs', '0009_itaboutmodels'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MobileService',
        ),
        migrations.DeleteModel(
            name='SiteStructureService',
        ),
        migrations.RenameField(
            model_name='mainservice',
            old_name='list_smm',
            new_name='ios_body',
        ),
        migrations.RenameField(
            model_name='mainservice',
            old_name='pages_smm',
            new_name='list_body',
        ),
        migrations.RenameField(
            model_name='mainservice',
            old_name='post_smm',
            new_name='page_body',
        ),
        migrations.RenameField(
            model_name='mainservice',
            old_name='photo_smm',
            new_name='pages_body',
        ),
        migrations.RemoveField(
            model_name='mainservice',
            name='video_smm',
        ),
        migrations.AddField(
            model_name='mainservice',
            name='photo_body',
            field=models.TextField(default=1, verbose_name='body'),
            preserve_default=False,
        ),
    ]
