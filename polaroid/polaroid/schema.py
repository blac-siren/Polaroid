import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug
import authentication.schema


class Query(authentication.schema.Query):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(authentication.schema.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query, mutation=Mutation)