# Generated by Django 5.1.1 on 2024-10-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mymedia'),
        ),
    ]
