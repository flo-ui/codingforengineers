# Generated by Django 3.1.2 on 2020-10-18 17:48

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201018_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', validators=[blog.validators.validate_file_type]),
        ),
    ]