# Generated by Django 5.2.4 on 2025-07-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_menuitem_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='ingredients',
            field=models.CharField(blank=True, verbose_name='İçindekiler'),
        ),
    ]
