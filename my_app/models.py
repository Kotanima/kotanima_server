# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db import models


class VkPost(models.Model):
    scheduled_date = models.CharField(max_length=10, null=True)
    phash = models.CharField(max_length=16, null=False)


class RedditPost(models.Model):
    # subreddit name
    sub_name = models.CharField(max_length=20, default=None, blank=True)

    # reddit post id
    post_id = models.CharField(max_length=6, blank=True)

    # author of reddit post
    author = models.CharField(max_length=20, blank=True)

    # reddit post title
    title = models.CharField(max_length=300, blank=True)

    # reddit url
    url = models.CharField(max_length=64, blank=True)

    # creation date
    created_utc = models.CharField(max_length=10, blank=True)

    # phase hash of the image, used to keep track of already existing photos
    # get rid of duplicates etc
    phash = models.CharField(max_length=16, null=True, blank=True)

    # image was manually checked/seen by human
    is_checked = models.BooleanField(default=False, null=False, blank=True)

    # image exists on disk in kotanima_content/static
    is_downloaded = models.BooleanField(default=False, null=False, blank=True)

    # image is manually not approved for posting
    is_disliked = models.BooleanField(default=False, null=False, blank=True)

    # image is sent to the checker app (to avoid sending data twice)
    is_selected = models.BooleanField(default=False, null=False, blank=True)

    # img wasnt downloaded/is a gif/corrupted etc
    wrong_format = models.BooleanField(default=False, blank=True)

    # link to original image
    source_link = models.TextField(default=None, null=True, blank=True)

    # tags in vk main post body
    visible_tags = ArrayField(models.CharField(max_length=9999), blank=True, null=True)

    # tags in photo description
    invisible_tags = ArrayField(models.CharField(max_length=9999), blank=True, null=True)

    # MyAnimeList id
    mal_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sub_name + " " + self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sub_name', 'post_id'], name="unique_post_in_sub")
        ]
        ordering = ['id']
