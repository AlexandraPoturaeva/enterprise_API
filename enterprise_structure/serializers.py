from rest_framework import serializers
from .models import Division, Employee, Position, Rule


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    subdivisions = serializers.SerializerMethodField()
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Division
        fields = [
            'id',
            'title',
            'parent_division',
            'created_at',
            'updated_at',
            'subdivisions',
            'employees',
        ]

    def get_subdivisions(self, obj):
        return DivisionSerializer(obj.get_children(), many=True).data

    def get_employees(self, obj):
        return EmployeeSerializer(obj.employee_set.all(), many=True).data


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
