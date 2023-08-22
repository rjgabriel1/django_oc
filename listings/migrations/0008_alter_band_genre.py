# Generated by Django 4.2.4 on 2023-08-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('DANCE', 'Dance'), ('POP', 'Pop'), ('R&B', 'Rnb'), ('CHRISTIAN', 'Christian')], default='HH', max_length=25),
        ),
    ]
