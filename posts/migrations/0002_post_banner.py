# Generated by Django 5.0.4 on 2024-04-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banner',
            field=models.ImageField(default='python.jpg', upload_to='posts/'),
        ),
    ]
