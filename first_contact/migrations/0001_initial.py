# Generated by Django 3.0.7 on 2020-06-26 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Contact_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=250)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_contact.Contact')),
            ],
            options={
                'db_table': 'contact_group',
            },
        ),
    ]
