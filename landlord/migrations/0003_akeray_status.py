# Generated by Django 4.0.5 on 2022-07-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0002_alter_akeray_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='akeray',
            name='status',
            field=models.CharField(choices=[('rented', 'Rented'), ('available', 'Available')], default='available', max_length=20),
        ),
    ]