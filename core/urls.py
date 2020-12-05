# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from graphene_django.views import GraphQLView
from core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this

    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
