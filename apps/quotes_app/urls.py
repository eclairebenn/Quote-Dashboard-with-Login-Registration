from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home), #success/home page
    url(r'^create$', views.create),
    url(r'^favorite/(?P<quote_id>\d+)$', views.favorite),
    url(r'^unfavorite/(?P<quote_id>\d+)$', views.unfavorite),
    ]