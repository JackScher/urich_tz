# Generated by Django 4.0.4 on 2022-05-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart_app', '0008_event_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
