# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin

from app.models import Order, Sale, Visit, Traffic
from app.models import Transaction


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ['id', 'count', 'amount', 'product_name', 'created_time']


@admin.register(Order)
class OrderAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'count', 'amount', 'created_time']
    search_fields = ['product_name']
    resource_class = OrderResource


class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale
        fields = ['id', 'amount', 'product_name', 'created_time']


@admin.register(Sale)
class SaleAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['product_name', 'amount', 'created_time']
    search_fields = ['product_name']
    resource_class = SaleResource


class VisitResource(resources.ModelResource):
    class Meta:
        model = Visit
        fields = ['id', 'page_name', 'visitors', 'unique_users', 'bounce_rate', 'bounce_rate_type', 'created_time']


@admin.register(Visit)
class VisitAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['page_name', 'visitors', 'unique_users', 'bounce_rate', 'bounce_rate_type', 'created_time']
    search_fields = ['page_name']
    resource_class = VisitResource


class TrafficResource(resources.ModelResource):
    class Meta:
        model = Traffic
        fields = ['id', 'referral', 'visitors', 'rate', 'rate_type', 'created_time']


@admin.register(Traffic)
class TrafficAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['referral', 'visitors', 'rate', 'rate_type', 'created_time']
    search_fields = ['referral']
    resource_class = TrafficResource


class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']


@admin.register(Transaction)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']
    resource_class = TransactionResource
