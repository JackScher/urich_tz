# Generated by Django 4.0.4 on 2022-05-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart_app', '0003_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
