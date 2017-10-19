from rest_framework import serializers
from .models import Query


class QuerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Query
        fields = (
            'id',
            'name',
            'description',
            'query',
            'creationdate',
            'tablename',
            'is_public'
        )