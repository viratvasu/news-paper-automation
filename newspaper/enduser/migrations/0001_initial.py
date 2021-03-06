# Generated by Django 3.0.8 on 2020-07-27 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paperboy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pno', models.CharField(max_length=10)),
                ('paper_boy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_boy', to='paperboy.PaperBoy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazines', models.ManyToManyField(to='newsadmin.Magazine')),
                ('news_papers', models.ManyToManyField(to='newsadmin.NewsPaper')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_subscription', to='enduser.UserProfile')),
            ],
        ),
    ]
