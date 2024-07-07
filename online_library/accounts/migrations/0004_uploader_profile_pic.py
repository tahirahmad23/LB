# Generated by Django 5.0 on 2024-06-24 14:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploader',
            name='profile_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile_pics'),
            preserve_default=False,
        ),
    ]