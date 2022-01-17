import graphene
from graphene_django import DjangoObjectType
from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track
        fields = "__all__"


class Query(graphene.ObjectType):
    tracks = graphene.List(graphene.NonNull(TrackType))

    def resolve_tracks(root, info, **kwargs):
        # Querying a list
        return Track.objects.all()


class CreateTrack(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    track = graphene.Field(TrackType) # return type of the mutation

    def mutate(root, info, title, description, url):
        if not info.context.user.is_authenticated:
            raise Exception('You must be logged in to create a track')
        
        track = Track.objects.create(title=title, description=description, url=url, posted_by=info.context.user)
        return CreateTrack(track=track)
    
    
class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
