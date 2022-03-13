# Generated by Django 3.2.9 on 2021-11-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
