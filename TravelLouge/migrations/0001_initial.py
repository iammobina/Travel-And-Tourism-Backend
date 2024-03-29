# Generated by Django 2.2.2 on 2019-11-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelLouge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=102)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
                ('image2', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
                ('image3', models.ImageField(default='travellouge/defualt.jpg', upload_to='image/%Y/%m/%d/')),
            ],
        ),
    ]
