from rest_framework.viewsets import ModelViewSet
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend

from .models import RedditPost, VkPost
from .serializers import RedditPostSerializer


class RedditPostFilter(ModelFilterSet):
    class Meta(object):
        model = RedditPost


class RedditPostViewSet(ModelViewSet):
    def get_queryset(self):
        qs = self.queryset
        # exclude posts that were already posted
        inner_qs = VkPost.objects.values_list('phash', flat=True)
        qs = qs.exclude(phash__in=inner_qs)

        qs = qs.filter(selected=False)
        qs = qs.filter(wrong_format=False)
        qs = qs.filter(dislike__isnull=True)
        qs = qs.order_by('?')  # todo rewrite because slow ...
        return qs

    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = RedditPostFilter


class RedditPostEditViewSet(ModelViewSet):
    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
