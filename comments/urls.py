from comments.views import CommentsViewSet
from rest_framework import routers
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'comments', CommentsViewSet, base_name="comments")

app_name = 'comments'

urlpatterns = [
    url(r'^', include(router.urls)),
]