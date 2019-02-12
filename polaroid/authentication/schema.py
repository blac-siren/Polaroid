import graphene
import graphql_jwt
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
# from django.contrib.auth.models import User
from .models import User

from django.contrib.auth import authenticate

class UserType(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True, )
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        new_user = User.objects.create_user(**kwargs)
        # user = new_user.authenticate(email=kwargs.get('email'), password=kwargs.get('password'))
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # if user is None:
        #     raise ValueError("Invalid....")
        return CreateUser(user=new_user)


class Query(graphene.ObjectType):

    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
