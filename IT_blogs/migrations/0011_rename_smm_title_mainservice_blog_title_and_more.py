# Generated by Django 4.0.4 on 2022-05-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_blogs', '0010_delete_mobileservice_delete_sitestructureservice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainservice',
            old_name='smm_title',
            new_name='blog_title',
        ),
        migrations.AlterField(
            model_name='mainservice',
            name='main_title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='services'),
        ),
    ]