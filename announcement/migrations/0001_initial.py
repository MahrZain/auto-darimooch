# Generated by Django 5.0.6 on 2024-06-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('buy_now', models.URLField(blank=True, null=True)),
            ],
        ),
    ]