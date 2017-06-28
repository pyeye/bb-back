from datetime import datetime

from rest_framework import generics

from .serializers import DaySaleSerializer
from .models import DaySaleRel


class SalesAPIView(generics.ListAPIView):
    serializer_class = DaySaleSerializer

    def get_queryset(self):
        today = datetime.now()
        queryset = DaySaleRel.objects.filter(month__date__month=today.month, month__date__year=today.year)
        return queryset
