import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
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

    @login_required
    def mutate(root, info, title, description, url):
        # if not info.context.user.is_authenticated:
        #     raise Exception('You must be logged in to create a track')
        
        track = Track.objects.create(title=title, description=description, url=url, posted_by=info.context.user)
        return CreateTrack(track=track)


class UpdateTrack(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    track = graphene.Field(TrackType)  # return type of the mutation

    @login_required
    def mutate(root, info, id, title, description, url):
        track = Track.objects.get(pk=id)
        
        if track.posted_by != info.context.user:
            raise Exception('You are not authorized to perform this action')
        
        track.title = title
        track.description = description
        track.url = url
        
        track.save()
        
        return UpdateTrack(track=track)
    

class DeleteTrack(graphene.Mutation):
    class Arguments:
        track_id = graphene.String(required=True)

    track_id = graphene.String()  # return type of the mutation

    @login_required
    def mutate(root, info, track_id):
        track = Track.objects.get(pk=track_id)

        if track.posted_by != info.context.user:
            raise Exception('You are not authorized to perform this action')

        track.delete()

        return DeleteTrack(track_id=track_id)
    
    
class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
