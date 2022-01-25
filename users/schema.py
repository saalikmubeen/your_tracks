import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql import GraphQLError
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude = ['password']


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.String(required=True))
    # me = graphene.Field(UserType, token=graphene.String(required=True)) # Per-argument token authentication
    me = graphene.Field(UserType)

    def resolve_user(root, info, **kwargs):
        return get_user_model().objects.get(pk=kwargs.get('id'))
    
    @login_required
    def resolve_me(root, info, **kwargs):
        user = info.context.user

        return user


class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)  # return type of the mutation

    def mutate(root, info, **kwargs):
        user = get_user_model()(
            username=kwargs.get('username'),
            email=kwargs.get('email')
        )
        user.set_password(kwargs.get('password'))
        user.save()
        return RegisterUser(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
