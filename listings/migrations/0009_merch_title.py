# Generated by Django 4.2.4 on 2023-08-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_band_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
