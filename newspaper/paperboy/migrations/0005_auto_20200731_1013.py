# Generated by Django 3.0.8 on 2020-07-31 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paperboy', '0004_deliverystatus_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverystatus',
            old_name='date',
            new_name='present_date',
        ),
    ]
