# Generated by Django 2.2.2 on 2019-12-26 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_leaderrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderrate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user'),
        ),
    ]
