from django.conf.urls import url
from blog.views import *

urlpatterns = [
     url(r'^$', PostLV.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)$', BookmarkDV.as_view(), name='detail'),
]
