# Generated by Django 5.1.3 on 2024-11-20 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=5)),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('faculties', models.ManyToManyField(related_name='students', to='management_app.faculty')),
                ('subjects', models.ManyToManyField(related_name='students', to='management_app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management_app.subject'),
        ),
    ]
