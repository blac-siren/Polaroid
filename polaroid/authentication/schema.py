import graphene
import graphql_jwt
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import User
from .tasks import Mail
from django.contrib.auth import authenticate

mail = Mail()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ('password')


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True, )
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        new_user = User.objects.create_user(**kwargs)
        return CreateUser(user=new_user)


class UserLogin(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        mail.delay(
            subject='Am the subject',
            message="Here is the message",
            sender=email,
            recipient_list=['zakariya.hussein@andela.com'])

        user = authenticate(
            request=info.context, email=email, password=password)
        return UserLogin(user=user)


class Query(graphene.ObjectType):

    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    user_login = UserLogin.Field()
