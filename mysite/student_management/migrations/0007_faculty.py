# Generated by Django 3.0.5 on 2021-04-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0006_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_name', models.TextField(max_length=25)),
                ('Subject_name', models.CharField(max_length=10)),
                ('Course_name', models.CharField(max_length=10)),
            ],
        ),
    ]
