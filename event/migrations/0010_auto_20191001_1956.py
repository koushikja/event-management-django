# Generated by Django 2.2.5 on 2019-10-01 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20191001_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_owner',
            field=models.ForeignKey(limit_choices_to={'user_type': 2}, on_delete=django.db.models.deletion.CASCADE, to='event.UserDetail'),
        ),
    ]
