# Generated by Django 4.2.4 on 2023-08-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_merch_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('ALTERNATIVE ROCK', 'Ar')], default='HH', max_length=25),
        ),
    ]
