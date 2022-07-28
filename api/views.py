from rest_framework import mixins, viewsets
from rest_framework import permissions
from .serializers import SchoolsSerializer, TweetsSerializer
from .filters import SchoolsFilter, TweetsFilter
from school.models import Schools
from tweets.models import Tweet

# Create your views here.

class SchoolsView(
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  viewsets.GenericViewSet,
):

  queryset = Schools.objects.all()
  serializer_class = SchoolsSerializer
  filterset_class = SchoolsFilter
  #permission_classes = [permissions.IsAuthenticated]


class TweetsView(
  mixins.CreateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  viewsets.GenericViewSet,
):

  queryset = Tweet.objects.all()
  serializer_class = TweetsSerializer
  filterset_class = TweetsFilter