# Generated by Django 5.1 on 2024-08-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(default=None, max_length=6, null=True),
        ),
    ]
