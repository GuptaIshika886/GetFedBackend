# Generated by Django 4.1.4 on 2023-03-24 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_registeredcntnowners'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canteen',
            name='c_feedback',
        ),
    ]
