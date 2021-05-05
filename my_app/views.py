from rest_framework.viewsets import ModelViewSet
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend

from .models import RedditPost, VkPost
from .serializers import RedditPostSerializer

from rest_framework.decorators import action
from rest_framework.response import Response


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
        # qs = qs.order_by('?')  # todo rewrite because slow ...
        return qs

    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = RedditPostFilter

    def get_approved_queryset(self):
        qs = RedditPost.objects.all()
        # exclude posts that were already posted
        qs = qs.filter(selected=False)
        qs = qs.filter(dislike=False)
        return qs

    def get_count_queryset(self):
        qs = RedditPost.objects.all()
        # exclude posts that were already posted
        qs = qs.filter(selected=False)
        qs = qs.filter(dislike__isnull=True)
        return qs

    @action(detail=False)
    def total_count(self, request):
        queryset = self.filter_queryset(self.get_count_queryset())
        count = queryset.count()
        content = {'count': count}
        return Response(content)

    @action(detail=False)
    def approved_count(self, request):
        queryset = self.filter_queryset(self.get_approved_queryset())
        count = queryset.count()
        content = {'count': count}
        return Response(content)


class RedditPostEditViewSet(ModelViewSet):
    queryset = RedditPost.objects.all()
    serializer_class = RedditPostSerializer
