# Generated by Django 4.0.5 on 2022-07-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0004_akeray_kebele_akeray_subcity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akeray',
            name='kebele',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
