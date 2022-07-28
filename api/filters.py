import django_filters
from school.models import Schools
from tweets.models import Tweet

class SchoolsFilter(django_filters.FilterSet):

  class Meta:
    model = Schools
    fields = ('__all__')


class TweetsFilter(django_filters.FilterSet):

  class Meta:
    model = Tweet
    fields = ('__all__')