# Generated by Django 5.0.6 on 2024-06-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]