from django.conf.urls import url, include
from rest_framework import routers

from general.views import UserViewSet#, ProfileViewSet
from comments.views import CommentsViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comments', CommentsViewSet, base_name="comments")
#router.register(r'profile', ProfileViewSet)

app_name='general'

urlpatterns = [
    url(r'^', include(router.urls)),
]