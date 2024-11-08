# Generated by Django 5.1.1 on 2024-09-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='mymedia')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
