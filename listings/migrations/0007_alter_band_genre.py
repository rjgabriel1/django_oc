# Generated by Django 4.2.4 on 2023-08-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('DANCE', 'Dance'), ('POP', 'Pop'), ('R&B', 'Rnb')], default='HH', max_length=25),
        ),
    ]
