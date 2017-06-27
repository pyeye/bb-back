from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from datetime import datetime

from .models import Event, Artist
from apps.sales.models import Sale


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
        return Sale.objects.values_list('name').filter(month__code=obj.date.month, day__code=weekday_code)

    class Meta:
        model = Event
        fields = ('pk', 'name', 'artists', 'info', 'date', 'start',
                  'discounts', 'is_special', 'poster', 'sales', 'extra')
