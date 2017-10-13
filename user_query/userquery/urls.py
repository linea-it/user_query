from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^userquery/$', views.UserQueryList.as_view()),
    url(r'^userquery/(?P<pk>[0-9]+)/$', views.UserQueryRetrieveUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)