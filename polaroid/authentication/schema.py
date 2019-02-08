import graphene
from graphene_django.types import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        new_user = User.objects.create_user(**kwargs)
        return CreateUser(user=new_user)

class Query(graphene.ObjectType):

    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
