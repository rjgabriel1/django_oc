# Generated by Django 4.2.4 on 2023-08-18 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_merch_alter_band_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
