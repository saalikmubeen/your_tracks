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
