from django.conf.urls import include, url
from django.contrib import admin

from .views import get_Data
import os

os.system('python views.py')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', get_Data, name='home'),
]
