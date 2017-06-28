from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from datetime import datetime

from .models import Event, Artist
from apps.sales.models import DaySaleRel


class ArtistSerializer(serializers.ModelSerializer):
    img = VersatileImageFieldSerializer(sizes='artist_img')

    class Meta:
        model = Artist
        fields = ('name', 'style', 'img')


class EventSerializer(serializers.ModelSerializer):
    poster = VersatileImageFieldSerializer(sizes='event_poster')
    artists = ArtistSerializer(many=True, read_only=True)
    sales = serializers.SerializerMethodField('get_today_sales')

    def get_today_sales(self, obj):
        weekday_code = obj.date.weekday() + 101
        return DaySaleRel.objects.values_list('sales__name').filter(
            month__date__month=obj.date.month,
            month__date__year=obj.date.year,
            day__code=weekday_code)

    class Meta:
        model = Event
        fields = ('pk', 'name', 'artists', 'info', 'date', 'start',
                  'discounts', 'is_special', 'poster', 'sales', 'extra')
