# Generated by Django 2.2.13 on 2020-06-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
