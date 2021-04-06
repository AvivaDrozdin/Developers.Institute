import django_filters
from accounts.models import Profile

class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        exclude = ['image']

