# Generated by Django 5.1.2 on 2024-10-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyAws', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.CharField(default='', max_length=450),
        ),
    ]
