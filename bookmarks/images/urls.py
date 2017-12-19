from django.conf.urls import url

from images import views

urlpatterns = [
    url(r'^create_pre/$', views.image_create_pre, name='create_pre'),
    url(r'^create/$', views.image_create, name='create'),
]
