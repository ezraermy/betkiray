# Generated by Django 4.0.5 on 2022-06-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akeray', '0002_renter_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('ordering',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(default=0),
        ),
    ]
