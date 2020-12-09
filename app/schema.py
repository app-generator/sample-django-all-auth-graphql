import graphene
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
# from graphene_django.types import DjangoObjectType

from app.models import Order, Sale


# class OrderType(DjangoObjectType):
#     class Meta:
#         model = Order


# class SaleType(DjangoObjectType):
#     class Meta:
#         model = Sale


class OrderMonthReportType(graphene.ObjectType):
    month = graphene.Int()
    total = graphene.Int(name='total')


class SalesMonthReportType(graphene.ObjectType):
    month = graphene.Int()
    total_amount = graphene.Float(name='total_amount')


class Query(graphene.ObjectType):
    # orders = graphene.List(
    #     OrderType,
    #     search=graphene.String(),
    #     first=graphene.Int(),
    #     skip=graphene.Int(),
    # )

    # sales = graphene.List(
    #     SaleType,
    #     search=graphene.String(),
    #     first=graphene.Int(),
    #     skip=graphene.Int(),
    # )

    orders_month_report = graphene.List(
        OrderMonthReportType,
        name='orders_month_report'
    )

    sales_month_report = graphene.List(
        SalesMonthReportType,
        name='sales_month_report'
    )

    # def resolve_orders(self, info, search=None, first=None, skip=None, **kwargs):
    #     queryset = Order.objects.all()
    #     if search:
    #         queryset = queryset.filter(product_name__icontains=search)
    #
    #     if skip:
    #         queryset = queryset[skip:]
    #
    #     if first:
    #         queryset = queryset[:first]
    #
    #     return queryset
    #
    # def resolve_sales(self, info, search=None, first=None, skip=None, **kwargs):
    #     queryset = Sale.objects.all()
    #     if search:
    #         queryset = queryset.filter(product_name__icontains=search)
    #
    #     if skip:
    #         queryset = queryset[skip:]
    #
    #     if first:
    #         queryset = queryset[:first]
    #
    #     return queryset

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
