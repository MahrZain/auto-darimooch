# Generated by Django 5.0.6 on 2024-07-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]