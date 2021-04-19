# myapi/urls.pyfrom django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'reddit_posts', views.RedditPostViewSet,
                basename='RedditModel')

router.register(r'edit_reddit_posts', views.RedditPostEditViewSet,
                basename='EditRedditModel')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),

]
