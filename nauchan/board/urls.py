from django.conf.urls import url, include
from views import ThreadListView


urlpatterns = [
    url(r'^(?P<string>[\w]{1, 3})/$', ThreadListView.as_view(), name='thread-list')
]
