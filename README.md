# Django Dashboard Argon

> **Open-Source Admin Dashboard** coded in **Django Framework** by **AppSeed** [Web App Generator](https://appseed.us/app-generator) - features:

- REST - simple node
- GraphQL - simple node
- Charts - bar chart and line chart
- (WIP) Datatables - pagination, search, inline edit (via Ajax) 
- (WIP) Social Login - AllAuth package integration for Google and Github 
- (WIP) Unitary Tests
- (WIP) Documentation 

<br />

## Base Requirements
- Install `django-import-export` package to import data form csv, xls and etc file to table.
```bash
$ pip install django-import-export
```
> Then add this package to INSTALLED_APPS in settings.py. Now you can change the admin section of each model and add this feature. so you can easily import the data to your table.


## REST Feature - Status OK

**Requirements**

To use REST in Django, install `djangorestframework`:
‍‍‍
```bash
$ pip install djangorestframework djangorestframework-simplejwt
```

In **[settings.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/core/settings.py)** add `rest_framework` in INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Then add django rest framework config in **[settings.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/core/settings.py)**:
```python
REST_FRAMEWORK = {
    'PAGE_SIZE': 5,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'COERCE_DECIMAL_TO_STRING': False,
}
```

> please add this package in requirements.txt

**Database/table structure**

We created two models to display the information in REST API, which includes `Visit` & `Traffic`:

```python
from django.db import models


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
    RATE_TYPE_UP = 1
    RATE_TYPE_DOWN = 2

    RATE_TYPE_CHOICES = [
        (RATE_TYPE_UP, 'up'),
        (RATE_TYPE_DOWN, 'down')
    ]

    referral = models.CharField(max_length=50)
    visitors = models.PositiveIntegerField()
    rate = models.FloatField()
    rate_type = models.SmallIntegerField(choices=RATE_TYPE_CHOICES)
    created_time = models.DateTimeField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'traffic'
        verbose_name_plural = 'traffics'
```

<br />

**Files** (that implements the feature)

- Create **[serializers.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/app/serializers.py)** file. Then add serializers `TrafficSerializer` and `VisitSerializer` as follows:
```python
from rest_framework import serializers
from app.models import Traffic, Visit


class TrafficSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
```

- In file **[views.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/app/views.py)** add the `TrafficViewSet` and `VisitViewSet` ViewSets.
```python
from rest_framework.viewsets import ModelViewSet
from app.models import Traffic, Visit
from app.serializers import TrafficSerializer, VisitSerializer


class TrafficViewSet(ModelViewSet):
    serializer_class = TrafficSerializer
    queryset = Traffic.objects.all()
    http_method_names = ['get']


class VisitViewSet(ModelViewSet):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
    http_method_names = ['get']
```

- In file **[urls.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/app/urls.py)**, add the following urls:
```python
from rest_framework import routers
from app.views import TrafficViewSet, VisitViewSet

router = routers.SimpleRouter()
router.register(r'api/v1/traffics', TrafficViewSet, basename="traffics")
router.register(r'api/v1/visits', VisitViewSet, basename="visits")

urlpatterns = router.urls + [
...
]
```

Now your REST APIs is ready. And you can use it.

<br />

**API structure**

The `traffics` and `visits` APIs structure follow the Django REST framework:

```json
{
    "count": "Total Item count",
    "next": "Next Link",
    "previous": "Previous Link",
    "results": "Serialized information in the form of a list"
}
```

**How to add data**

In Django admin, you can import data for the **Visits** and **Traffics** sections. 
To do this just click on ```IMPORT``` button in each section, then select your csv, xls or etc file and submit it.

![Import Data](https://raw.githubusercontent.com/app-generator/django-simple-charts/master/media/admin_import.png)

> Download **[Visits](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/sample_data/visits.csv)** and **[Traffics](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/sample_data/traffics.csv)** Sample data

**How to consume API**

* To use AIPs, you can import the sample **[POSTMAN](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/postman/postman.json)**

<br />

## GraphQL Feature - Status OK

**Requirements**

To use GraphQL in Django install `graphene-django`:
```bash
$ pip install graphene-django
```

In **[settings.py](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/core/settings.py)** add `graphene-django` in INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'graphene_django',
]
```

**Database/table structure**

We created two models to display the information in GraphQL API, which includes `Order` & `Sale`:

```python
from django.db import models


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
```

<br />

**Files** (that implements the feature)

- Create the **[schema.py]()** file in your app. Then add the following classes to make your own schema:
> These classes include monthly reports on sales and orders.
```python
import graphene
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from app.models import Order, Sale


class OrderMonthReportType(graphene.ObjectType):
    month = graphene.Int()
    total = graphene.Int(name='total')


class SalesMonthReportType(graphene.ObjectType):
    month = graphene.Int()
    total_amount = graphene.Float(name='total_amount')


class Query(graphene.ObjectType):
    orders_month_report = graphene.List(
        OrderMonthReportType,
        name='orders_month_report'
    )

    sales_month_report = graphene.List(
        SalesMonthReportType,
        name='sales_month_report'
    )

    def resolve_orders_month_report(self, info, **kwargs):
        queryset = Order.objects.annotate(
            date=TruncMonth('created_time')
        ).values('date').annotate(total=Count('id')).values('date', 'total').order_by('date')

        report = {month: 0 for month in range(1, 13)}
        for order_month in queryset:
            report[order_month['date'].month] += order_month['total']
        report = sorted(report.items())

        res = []
        for month, total in report:
            res.append({'month': month, 'total': total})

        return res

    def resolve_sales_month_report(self, info, **kwargs):
        queryset = Sale.objects.annotate(
            date=TruncMonth('created_time')
        ).values('date').annotate(total_amount=Sum('amount')).values('date', 'total_amount').order_by('date')

        report = {month: 0 for month in range(1, 13)}
        for order_month in queryset:
            report[order_month['date'].month] += round(order_month['total_amount'], 2)
        report = sorted(report.items())

        res = []
        for month, total_amount in report:
            res.append({'month': month, 'total_amount': total_amount})

        return res
```

- To receive data through any app, you need to create a [schema.py]() file in the main app. In this project, the name of the main app is `core`. So in this part, I created a scheam.py:
```python
import graphene
from app.schema import Query as app_query


class Query(app_query):
    pass


schema = graphene.Schema(query=Query)
```

- Then add the url in [urls.py]() in main app:
```python
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from core.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This is our GraphQL URL
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
```
> We enabled ‍‍‍`graphiql` to run queries with `graphiql=True`

- Now you can open `http://localhost:8000/graphql/` in your browser and run your queries.

Sample Query:
```text
{
  orders_month_report{
    total
    month
  }
  sales_month_report{
    total_amount
    month
  }
}
```

<br />

**API structure**

The `orders` and `sales` APIs structure follow the Django GraphQL:
```json
{
  "data": {  # "GraphQL data in the form of a list"
    "orders_month_report": [],
    "sales_month_report": []
  }
}
```

**How to add data**

In Django admin, you can import data for the **Orders** and **Sales** sections. 
To do this just click on ```IMPORT``` button in each section, then select your csv, xls or etc file and submit it.

![Import Data](https://raw.githubusercontent.com/app-generator/django-simple-charts/master/media/admin_import.png)

> Download **[Orders](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/sample_data/orders.csv)** and **[Sales](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/sample_data/sales.csv)** Sample data


**How to consume API**

* To use AIPs, you can import the sample **[POSTMAN](https://github.com/app-generator/django-dashboard-argon-eps/blob/master/media/postman/postman.json)**

<br />

## Bar Chart Sample - Status OK 

**Database/table structure**

@Todo

<br />

**Files** (that implements the feature)

- Link to file(s)

<br />

**How to add data on tables**

@Todo

## Line Chart Sample - Status OK 

**Database/table structure**

@Todo

<br />

**Files** (that implements the feature)

- Link to file(s)

<br />

**How to add data on tables**

@Todo

## Social Login (WIP)

**Database/table structure**

@Todo

<br />

**Files** (that implements the feature)

- Link to file(s)

<br />

## Unitary Tests - Status WIP

- **How to test feature 1**
- **How to test feature 2**
- **How to test feature 3**

<br />

## Full Documentation (WIP) 

This section will point users to https://docs.appseed.us (WIP)

<br />

---
Django Dashboard Argon - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
