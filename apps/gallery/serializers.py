from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Album, Image


class ImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='gallery_image')

    class Meta:
        model = Image
        fields = ('image', )


class AlbumSerializer(serializers.ModelSerializer):
    main_image = VersatileImageFieldSerializer(sizes='album_image')
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'date', 'main_image', 'images')


class GallerySerializer(serializers.ModelSerializer):
    main_image = VersatileImageFieldSerializer(sizes='album_image')
    image_count = serializers.IntegerField(source='images.count', read_only=True)

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'date', 'main_image', 'image_count')
