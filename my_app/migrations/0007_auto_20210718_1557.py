# Generated by Django 3.2.5 on 2021-07-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_auto_20210418_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redditpost',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='redditpost',
            name='selected',
        ),
        migrations.AddField(
            model_name='redditpost',
            name='is_checked',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='redditpost',
            name='is_disliked',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='redditpost',
            name='is_downloaded',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='redditpost',
            name='is_selected',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='redditpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vkpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
