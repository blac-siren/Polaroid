import graphene
import authentication.schema


class Query(authentication.schema.Query):
    pass


schema = graphene.Schema(query=Query)