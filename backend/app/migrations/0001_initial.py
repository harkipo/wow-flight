# Generated by Django 3.1.4 on 2021-03-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('departure_city', models.CharField(blank=True, max_length=255, null=True)),
                ('departure_time', models.IntegerField(blank=True, null=True)),
                ('arrival_city', models.CharField(blank=True, max_length=255, null=True)),
                ('arrival_time', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flight',
            },
        ),
    ]
