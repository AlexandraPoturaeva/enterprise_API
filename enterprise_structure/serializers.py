from rest_framework import serializers
from .models import Division


class DivisionSerializer(serializers.ModelSerializer):
    subdivisions = serializers.SerializerMethodField()

    class Meta:
        model = Division
        fields = [
            'id',
            'title',
            'parent_division',
            'created_at',
            'updated_at',
            'subdivisions',
        ]

    def get_subdivisions(self, obj):
        return DivisionSerializer(obj.get_children(), many=True).data
