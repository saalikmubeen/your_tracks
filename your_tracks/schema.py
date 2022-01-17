import graphene

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
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
