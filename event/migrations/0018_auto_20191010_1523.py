# Generated by Django 2.2.5 on 2019-10-10 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_auto_20191010_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects-images/'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
