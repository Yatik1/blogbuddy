# Generated by Django 5.0.4 on 2024-04-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
