from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Month, Day, Sale


class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = ('name', 'code')


class SaleSerializer(serializers.ModelSerializer):
    day = DaySerializer(read_only=True)
    image = VersatileImageFieldSerializer(sizes='sales_image')

    class Meta:
        model = Sale
        fields = ('day', 'name', 'info', 'image')


class MonthSerializer(serializers.ModelSerializer):
    sales = SaleSerializer(many=True, read_only=True)

    class Meta:
        model = Month
        fields = ('pk', 'name', 'sales')
