# Generated by Django 4.0.1 on 2022-01-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Markers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
