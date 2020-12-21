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
To use REST in Django, we'll use `djangorestframework`. To install this package, please follow the procedure below:
‍‍‍
```bash
$ pip install djangorestframework djangorestframework-simplejwt
```

In **[settings.py]()** add `rest_framework` in INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Then add django rest framework config in **[settings.py]()**:
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

- Create **[serializers.py]()** file. Then add serializers `TrafficSerializer` and `VisitSerializer` as follows:
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

- In file **[views.py]()**, add the `TrafficViewSet` and `VisitViewSet` ViewSets.
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

- In file **[urls.py]()**, add the following urls:
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

> Download **[Visits]()** and **[Traffics]()** Sample data

**How to consume API**

* To use AIPs, you can import the sample **[POSTMAN]()**

<br />

## GraphQL Feature - Status OK

**Database/table structure**

@Todo

<br />

**Files** (that implements the feature)

- Link to file(s)

<br />

**API structure**

@Todo

**How to add data**

@Todo

**How to consume API**

@Todo - Using POSTMAN

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
