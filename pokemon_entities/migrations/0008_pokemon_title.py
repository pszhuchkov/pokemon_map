# Generated by Django 3.1.4 on 2020-12-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20201224_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
