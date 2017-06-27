from rest_framework import viewsets, generics

from .serializers import MenuSerializer, CategorySerializer
from .models import Menu, Category


class MenuViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = MenuSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Menu.related_objects.filter(is_active=True)
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__code=category)
        return queryset


class CategoryAPIView(generics.ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Category.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group__code=group)
        return queryset

