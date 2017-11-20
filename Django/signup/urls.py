from django.conf.urls import url
from . import views

urlpatterns = [
    # /signup/
    url(r'^$', views.index, name='index'),
]