# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db import models


class VkPost(models.Model):
    scheduled_date = models.CharField(max_length=10, null=True)
    phash = models.CharField(max_length=16, null=False)


class RedditPost(models.Model):
    sub_name = models.CharField(max_length=20, default=None, blank=True)
    post_id = models.CharField(max_length=6, blank=True)
    author = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=64, blank=True)
    created_utc = models.CharField(max_length=10, blank=True)
    phash = models.CharField(max_length=16, null=True, blank=True)
    dislike = models.BooleanField(default=None, null=True, blank=True)
    wrong_format = models.BooleanField(default=False, blank=True)
    selected = models.BooleanField(default=None, null=True, blank=True)
    source_link = models.TextField(default=None, null=True, blank=True)
    visible_tags = ArrayField(models.CharField(max_length=9999), blank=True, null=True)
    invisible_tags = ArrayField(models.CharField(max_length=9999), blank=True, null=True)
    mal_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sub_name + " " + self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sub_name', 'post_id'], name="unique_post_in_sub")
        ]
        ordering = ['id']
