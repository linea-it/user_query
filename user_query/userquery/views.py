from .models import Query
from .serializers import UserQuerySerializer
from rest_framework import generics


class UserQueryList(generics.ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = UserQuerySerializer


class UserQueryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = UserQuerySerializer