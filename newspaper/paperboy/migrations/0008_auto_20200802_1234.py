# Generated by Django 3.0.8 on 2020-08-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperboy', '0007_paperboy_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperboy',
            name='pincode',
            field=models.IntegerField(default=524341),
        ),
    ]