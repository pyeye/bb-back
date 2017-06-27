from rest_framework import viewsets

from .serializers import MonthSerializer
from .models import Month


class SalesViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = MonthSerializer
    lookup_field = 'code'

    def get_queryset(self):
        queryset = Month.related_objects.all()
        month = self.request.query_params.get('month', None)
        if month is not None:
            queryset = queryset.filter(code=month)
        return queryset

