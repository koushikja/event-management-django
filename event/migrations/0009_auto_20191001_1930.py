# Generated by Django 2.2.5 on 2019-10-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20191001_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_type',
            field=models.CharField(choices=[(1, 'user'), (2, 'lessor'), (3, 'service')], default=1, max_length=10),
        ),
    ]
