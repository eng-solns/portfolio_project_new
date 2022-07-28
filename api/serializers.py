from rest_framework.serializers import ModelSerializer
from school.models import Schools
from tweets.models import Tweet


class SchoolsSerializer(ModelSerializer):
  class Meta:
    model = Schools
    fields = ('__all__')

class TweetsSerializer(ModelSerializer):
  class Meta:
    model = Tweet
    fields = ('__all__')