# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime

from django.test import TestCase
from django.test import Client

from app.models import Traffic, Visit, Order, Sale

client = Client()


class RESTAPIsTest(TestCase):

    def test_traffic(self):
        response = client.get('/api/v1/traffics/')
        self.assertEqual(response.json().get('count'), 0, 'Traffics API: failure in fetching data.')

        traffic_data = {
            'referral': 'Facebook',
            'visitors': 3,
            'rate': 18.5,
            'rate_type': Traffic.BOUNCE_RATE_TYPE_UP,
            'created_time': datetime.now()
        }
        Traffic.objects.create(**traffic_data)

        response = client.get('/api/v1/traffics/')
        self.assertEqual(response.json().get('count'), 1, 'Traffics API: failure in fetching data.')
        self.assertEqual(response.json().get('results')[0]['referral'], 'Facebook', 'Traffics API: data is wrong.')

    def test_visit(self):
        response = client.get('/api/v1/visits/')
        self.assertEqual(response.json().get('count'), 0, 'Visits API: failure in fetching data.')

        visit_data = {
            'page_name': '/argon/',
            'visitors': 3,
            'unique_users': 340,
            'bounce_rate': 18.5,
            'bounce_rate_type': Visit.BOUNCE_RATE_TYPE_UP,
            'created_time': datetime.now()
        }
        Visit.objects.create(**visit_data)

        response = client.get('/api/v1/visits/')
        self.assertEqual(response.json().get('count'), 1, 'Visits API: failure in fetching data.')
        self.assertEqual(response.json().get('results')[0]['page_name'], '/argon/', 'Visits API: data is wrong.')


class GraphQLAPIsTest(TestCase):
    def test_orders_report(self):
        order_data = {
            'count': 3,
            'amount': 18.50,
            'product_name': 'GUILD',
            'created_time': datetime.now()
        }
        Order.objects.create(**order_data)

        payload = {
            "query": "query {orders_month_report {month total}}",
            "variables": {}
        }
        response = client.post('/graphql/', payload, format='json')
        self.assertEqual(len(response.json().get('data').get('orders_month_report')), 12,
                         'Orders API: failure in fetching data.')

    def test_sales_report(self):
        sale_data = {
            'amount': 18.50,
            'product_name': 'GUILD',
            'created_time': datetime.now()
        }
        Sale.objects.create(**sale_data)

        payload = {
            "query": "query {sales_month_report {month total_amount}}",
            "variables": {}
        }
        response = client.post('/graphql/', payload, format='json')
        self.assertEqual(len(response.json().get('data').get('sales_month_report')), 12,
                         'Sales API: failure in fetching data.')
