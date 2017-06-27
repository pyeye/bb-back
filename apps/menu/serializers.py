from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Menu, Price, Category, Group, Image


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ('count', 'measure', 'value')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'code')


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='menu_image')

    class Meta:
        model = Image
        fields = ('image', )


class CategorySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'code', 'images', 'template')


class MenuSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('pk', 'name', 'description', 'category', 'created_at', 'prices')
