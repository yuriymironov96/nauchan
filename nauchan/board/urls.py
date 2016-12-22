from django.conf.urls import url, include
from views import ThreadListView, ThreadView


urlpatterns = [
    url(r'^(?P<board>[a-z]{1,3})/$',
                                ThreadListView.as_view(), name='thread-list'),
    url(r'^(?P<board>[a-z]{1,3})/(?P<thread_id>[1-9]{1,3})/$',
                                    ThreadView.as_view(), name='thread-view'),
]
