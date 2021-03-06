# Generated by Django 3.1.6 on 2021-04-17 11:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedditPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(default=None, max_length=20)),
                ('post_id', models.CharField(max_length=6)),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=64)),
                ('created_utc', models.CharField(max_length=10)),
                ('phash', models.CharField(max_length=16, null=True)),
                ('dislike', models.BooleanField(default=None, null=True)),
                ('wrong_format', models.BooleanField(default=False)),
                ('selected', models.BooleanField(default=False)),
                ('source_link', models.TextField(default=None, null=True)),
                ('visible_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=9999), blank=True, size=None)),
                ('invisible_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=9999), blank=True, size=None)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='VkPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.CharField(max_length=10, null=True)),
                ('phash', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddConstraint(
            model_name='redditpost',
            constraint=models.UniqueConstraint(fields=('sub_name', 'post_id'), name='unique_post_in_sub'),
        ),
    ]
