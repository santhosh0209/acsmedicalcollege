# Generated by Django 2.2.10 on 2020-11-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0002_main_event_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_event',
            name='title',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='main_event',
            name='unique_id',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
    ]
