# Generated by Django 3.1.7 on 2021-03-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0002_auto_20210313_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='picture',
        ),
        migrations.AddField(
            model_name='film',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]