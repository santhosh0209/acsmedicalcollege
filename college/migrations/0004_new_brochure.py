# Generated by Django 3.1.2 on 2020-11-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20201119_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='brochure',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='brochure'),
        ),
    ]
