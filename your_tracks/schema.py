import graphene
import graphql_jwt

import tracks.schema
import users.schema

class Query(
    tracks.schema.Query,  # Add your Query objects here
    users.schema.Query,
    graphene.ObjectType
):
    pass

class Mutation(
    tracks.schema.Mutation,
    users.schema.Mutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
