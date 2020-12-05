import graphene
from graphene_django.types import DjangoObjectType

from app.models import Order, Sale


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class SaleType(DjangoObjectType):
    class Meta:
        model = Sale


class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)
    sales = graphene.List(SaleType)

    def resolve_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_sales(self, info, **kwargs):
        return Sale.objects.all()
