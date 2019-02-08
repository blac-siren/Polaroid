import graphene
from graphene_django.types import DjangoObjectType
from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'istartswith'],
            'email': ['exact'],
            'password': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


# class UserCreateInput(graphene.InputObjectType):


class UserCreate(graphene.relay.ClientIDMutation):
    class Input:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    new_user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = User.objects.create_user(**input)
        user.save
        return cls(new_user=user)


class Query(graphene.ObjectType):
    user = graphene.List(UserNode)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class Mutation(graphene.ObjectType):
    create_user = UserCreate.Field()
