# Generated by Django 3.0.7 on 2020-07-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]