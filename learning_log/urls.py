# from multiprocessing.dummy import Namespace
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('users/',include(('users.urls','users'),namespace='users')),
    url('^',include(('learning_logs.urls','learning_logs'),namespace='learning_logs')),

]
