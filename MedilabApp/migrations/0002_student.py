# Generated by Django 5.0.6 on 2024-07-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedilabApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]