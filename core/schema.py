import graphene
from app.schema import Query as app_query


class Query(app_query):
    pass


schema = graphene.Schema(query=Query)
