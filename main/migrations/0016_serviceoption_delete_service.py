# Generated by Django 5.2.4 on 2025-07-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_type', models.CharField(choices=[('dugun', 'Düğün'), ('nisan', 'Nişan')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('price', models.PositiveIntegerField()),
                ('per_person', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
