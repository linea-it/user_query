from .models import Query
from .serializers import QuerySerializer
from rest_framework import viewsets


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
