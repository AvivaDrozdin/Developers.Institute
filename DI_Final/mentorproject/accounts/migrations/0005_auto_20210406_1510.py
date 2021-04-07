# Generated by Django 3.1.7 on 2021-04-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210406_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human_language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='human_language',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='human_language',
            field=models.ManyToManyField(to='accounts.Human_language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ManyToManyField(to='accounts.Location'),
        ),
    ]
