# Generated by Django 2.2.6 on 2019-11-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0005_auto_20191114_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/img/anonymous-user.png', null=True, upload_to='media/user_images'),
        ),
    ]
