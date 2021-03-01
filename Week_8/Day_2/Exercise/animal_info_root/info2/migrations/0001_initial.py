# Generated by Django 3.1.7 on 2021-03-01 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Families',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('max_speed', models.FloatField(default=0)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info2.families')),
            ],
        ),
    ]
