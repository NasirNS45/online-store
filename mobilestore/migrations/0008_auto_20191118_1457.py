# Generated by Django 2.2.6 on 2019-11-18 14:57

from django.db import migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0007_auto_20191118_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=django_fields.fields.DefaultStaticImageField(blank=True, null=True, upload_to='user_images'),
        ),
    ]
