# Generated by Django 5.1.2 on 2024-12-09 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='personaltable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=400)),
                ('Email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('Type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Loginid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.logintable')),
            ],
        ),
    ]