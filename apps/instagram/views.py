from rest_framework import viewsets

from .serializers import InstagramSerializer
from .models import Instagram


class InstagramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = InstagramSerializer

    def get_queryset(self):
        queryset = Instagram.related_objects.all()
        return queryset