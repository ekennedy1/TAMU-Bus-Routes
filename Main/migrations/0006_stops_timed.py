# Generated by Django 4.0.3 on 2022-04-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_rename_offcampus_routes_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='stops',
            name='timed',
            field=models.BooleanField(default=0),
        ),
    ]