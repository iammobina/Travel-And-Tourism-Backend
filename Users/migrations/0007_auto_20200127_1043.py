# Generated by Django 2.2.2 on 2020-01-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20200127_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='freetimes',
        ),
        migrations.AddField(
            model_name='leader',
            name='freetimes',
            field=models.ManyToManyField(to='Users.TimeOBJ'),
        ),
    ]
