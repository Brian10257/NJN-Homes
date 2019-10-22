# Generated by Django 2.2.6 on 2019-10-22 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_single', models.CharField(max_length=500)),
                ('property_single_id', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
