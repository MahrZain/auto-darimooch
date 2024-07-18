# Generated by Django 5.0.6 on 2024-06-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='message',
            field=models.CharField(blank=True, help_text='Only One Statement Show at A Time', max_length=200, null=True),
        ),
    ]