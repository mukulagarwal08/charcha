# Generated by Django 2.1.4 on 2018-12-30 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20181230_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='owner',
        ),
    ]
