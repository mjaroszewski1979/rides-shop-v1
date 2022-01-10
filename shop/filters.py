import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):

    class Meta:
        model = Car
        fields = ('producer', 'country_of_origin', 'colour', 'production_year', 'number_of_doors', 'electric', 'first_owner')