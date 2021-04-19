# serializers.py
from rest_framework import serializers

from .models import RedditPost


class RedditPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = RedditPost
        fields = ['id', 'sub_name', 'post_id',
                  'author', 'title', 'url',
                  'created_utc', 'phash',
                  'dislike', 'wrong_format',
                  'selected', 'source_link',
                  'visible_tags', 'invisible_tags']
