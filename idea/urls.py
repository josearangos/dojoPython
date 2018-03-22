from django.conf.urls import url
from idea.views import *

urlpatterns=[
    url(r'^idea/$',ideaList.as_view(), name='idea')
]