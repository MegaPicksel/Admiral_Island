from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from admiral_island import views

urlpatterns = [
    url(r'^$', views.home_redirect, name='home_redirect'),
    url(r'^info/', include ('info.urls')),
    path('admin/', admin.site.urls),
]
