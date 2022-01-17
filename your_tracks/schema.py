import graphene

import tracks.schema


class Query(
    tracks.schema.Query,  # Add your Query objects here
    graphene.ObjectType
):
    pass



schema = graphene.Schema(query=Query)
