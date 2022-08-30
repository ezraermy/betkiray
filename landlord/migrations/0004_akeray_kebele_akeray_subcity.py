# Generated by Django 4.0.5 on 2022-07-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0003_akeray_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='akeray',
            name='kebele',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='akeray',
            name='subcity',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]