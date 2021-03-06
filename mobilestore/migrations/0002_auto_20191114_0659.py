# Generated by Django 2.2.6 on 2019-11-14 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobilestore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='mobilestore.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='mobilestore.ProductCategory'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
