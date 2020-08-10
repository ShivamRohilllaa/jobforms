# Generated by Django 3.0.8 on 2020-08-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clgdet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='othdet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefloc', models.CharField(max_length=100)),
                ('curloc', models.CharField(max_length=15)),
                ('pskills', models.CharField(max_length=100)),
                ('sskills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
