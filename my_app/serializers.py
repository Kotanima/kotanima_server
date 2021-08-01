# serializers.py
from rest_framework import serializers

from .models import RedditPost


class RedditPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPost
        fields = [
            "id",
            "sub_name",
            "post_id",
            "author",
            "title",
            "url",
            "created_utc",
            "phash",
            "wrong_format",
            "source_link",
            "mal_id",
            "is_checked",
            "is_selected",
            "is_disliked",
            "is_downloaded",
            "visible_tags",
            "invisible_tags",
        ]
