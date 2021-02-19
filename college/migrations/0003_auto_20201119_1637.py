# Generated by Django 3.1.2 on 2020-11-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20201119_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(default=None)),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='news')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
