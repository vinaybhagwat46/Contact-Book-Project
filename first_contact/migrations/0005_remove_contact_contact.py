# Generated by Django 3.0.7 on 2020-08-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_contact', '0004_auto_20200710_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact',
        ),
    ]
