from .models import UserQuery
from .serializers import UserQuerySerializer
from rest_framework import generics


class UserQueryList(generics.ListCreateAPIView):
    queryset = UserQuery.objects.all()
    serializer_class = UserQuerySerializer


class UserQueryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserQuery.objects.all()
    serializer_class = UserQuerySerializer