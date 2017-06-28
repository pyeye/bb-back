from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Month, Day, Sale, DaySaleRel


class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = ('name', 'code')


class SaleSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='sales_image')

    class Meta:
        model = Sale
        fields = ('name', 'info', 'image')


class DaySaleSerializer(serializers.ModelSerializer):
    day = DaySerializer(read_only=True)
    sales = SaleSerializer(many=True, read_only=True)

    class Meta:
        model = DaySaleRel
        fields = ('day', 'sales')


class MonthSerializer(serializers.ModelSerializer):
    day_sales = DaySaleSerializer(many=True, read_only=True)

    class Meta:
        model = Month
        fields = ('pk', 'date', 'day_sales')
