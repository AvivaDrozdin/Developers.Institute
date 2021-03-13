# Generated by Django 3.1.7 on 2021-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='Category',
            new_name='category',
        ),
        migrations.AddField(
            model_name='film',
            name='picture',
            field=models.URLField(default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fuser-images.githubusercontent.com%2F24848110%2F33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png&f=1&nofb=1', max_length=500),
        ),
    ]
