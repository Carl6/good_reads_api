from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BookList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', BookDetail.as_view()),
    url(r'^authors/$', BookAuthorList.as_view())
]

