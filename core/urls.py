# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this

    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
