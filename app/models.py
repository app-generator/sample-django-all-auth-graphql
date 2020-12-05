# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    count = models.PositiveIntegerField()
    amount = models.FloatField(db_index=True)
    product_name = models.CharField(max_length=40, db_index=True)
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class Sale(models.Model):
    amount = models.FloatField(db_index=True)
    product_name = models.CharField(max_length=40, db_index=True)
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'sales'


class Visit(models.Model):
    BOUNCE_RATE_TYPE_UP = 1
    BOUNCE_RATE_TYPE_DOWN = 2

    BOUNCE_RATE_TYPE_CHOICES = [
        (BOUNCE_RATE_TYPE_UP, 'up'),
        (BOUNCE_RATE_TYPE_DOWN, 'down')
    ]

    page_name = models.CharField(max_length=255)
    visitors = models.PositiveIntegerField()
    unique_users = models.PositiveIntegerField()
    bounce_rate = models.FloatField()
    bounce_rate_type = models.SmallIntegerField(choices=BOUNCE_RATE_TYPE_CHOICES)
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'visit'
        verbose_name_plural = 'visits'


class Traffic(models.Model):
    BOUNCE_RATE_TYPE_UP = 1
    BOUNCE_RATE_TYPE_DOWN = 2

    BOUNCE_RATE_TYPE_CHOICES = [
        (BOUNCE_RATE_TYPE_UP, 'up'),
        (BOUNCE_RATE_TYPE_DOWN, 'down')
    ]

    referral = models.CharField(max_length=50)
    visitors = models.PositiveIntegerField()
    rate = models.FloatField()
    rate_type = models.SmallIntegerField(choices=BOUNCE_RATE_TYPE_CHOICES)
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'traffic'
        verbose_name_plural = 'traffics'
