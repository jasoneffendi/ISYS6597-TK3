#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework import routers

from api.views.reporting_views import ReportingViewset

router = routers.DefaultRouter()
router.register(r'reporting', ReportingViewset, basename='reporting')

urlpatterns = [
    url(r'^', include(router.urls, namespace=''))
]
