# Generated by Django 2.2.6 on 2020-01-31 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_articlepost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='permit_group',
            field=models.IntegerField(default=0),
        ),
    ]
