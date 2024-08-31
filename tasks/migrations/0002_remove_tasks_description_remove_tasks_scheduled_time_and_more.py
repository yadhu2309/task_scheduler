# Generated by Django 5.1 on 2024-08-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='scheduled_time',
        ),
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(default='2024-08-23'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='end_time',
            field=models.TimeField(default='11:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='start_time',
            field=models.TimeField(default='09:00:00'),
            preserve_default=False,
        ),
    ]
