# Generated by Django 3.0.8 on 2020-07-31 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperboy', '0002_paperboy_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]