# Generated by Django 4.2.16 on 2024-09-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cniapp', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
