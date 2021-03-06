# Generated by Django 3.1.7 on 2021-04-06 09:54

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210406_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='human_language',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ENG', 'English'), ('HEB', 'עברית'), ('ARA', 'العربية'), ('RUS', 'Русский'), ('ESP', 'Spanish'), ('FRE', 'Français')], default='English', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('online', 'Online'), ('tlv', 'Tel Aviv District'), ('central', 'Central District'), ('jerusalem', 'Jerusalem District'), ('haifa', 'Haifa District'), ('north', 'Northern District'), ('south', 'Southern District')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills_have',
            field=models.ManyToManyField(blank=True, related_name='existing', to='accounts.Skill'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills_wanted',
            field=models.ManyToManyField(blank=True, related_name='needed', to='accounts.Skill'),
        ),
    ]
