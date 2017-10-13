from rest_framework import serializers
from .models import UserQuery


class UserQuerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = UserQuery
        fields = (
            'id',
            'name',
            'description',
            'query',
            'creationdate',
            'tablename',
            'is_public'
        )