from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from image_cropping.utils import get_backend

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
    main_image = serializers.SerializerMethodField('get_images')
    image_count = serializers.IntegerField(source='images.count', read_only=True)

    def get_images(self, obj):
        thumbnail_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (600, 0),
                'box': obj.cropping,
                'crop': True,
            }
        )
        original_url = get_backend().get_thumbnail_url(
            obj.main_image,
            {
                'size': (1900, 0),
                'box': obj.cropping,
                'crop': True,
            }
        )
        return {'thumbnail': thumbnail_url, 'original': original_url}

    class Meta:
        model = Album
        fields = ('pk', 'name', 'description', 'date', 'main_image', 'image_count')
