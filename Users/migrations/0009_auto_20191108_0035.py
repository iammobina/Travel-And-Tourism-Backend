# Generated by Django 2.2.2 on 2019-11-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20191108_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, height_field=100, upload_to='media/image/profile', width_field=100),
        ),
    ]
