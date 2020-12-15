# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from rest_framework import routers

from app.views import TrafficViewSet, VisitViewSet

router = routers.SimpleRouter()
router.register(r'api/v1/traffics', TrafficViewSet, basename="traffics")
router.register(r'api/v1/visits', VisitViewSet, basename="visits")

urlpatterns = router.urls + [
    # The home page
    path('', views.index, name='home'),

    # transactions
    re_path(r'^transactions/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.TransactionView.as_view(),
            name='transactions'),

    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),
]
