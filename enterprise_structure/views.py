from rest_framework import viewsets
from .models import Division, Employee, Position, Rule
from .serializers import (
    DivisionSerializer,
    EmployeeSerializer,
    PositionSerializer,
    RuleSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from mptt.exceptions import InvalidMove


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(parent_division=None)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        parent_division = request.data.get('parent_division')
        if parent_division is None:
            if self.queryset:
                return Response(
                    data='Root division already exists. '
                         'Provide parent_division',
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        return super().create(request)

    def update(self, request, *args, **kwargs):
        try:
            super().update(request)
        except InvalidMove as exc:
            return Response(
                data=str(exc),
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

        return super().update(request)

    def destroy(self, request, *args, **kwargs):
        division = self.get_object()
        employees = division.employee_set.all()
        if employees:
            return Response(
                data='There are employees '
                     'at this division or its subdivisions. '
                     'Delete employees first to delete division',
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

        return super().destroy(request)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class RuleViewSet(viewsets.ModelViewSet):
    serializer_class = RuleSerializer
    queryset = Rule.objects.all()


class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def destroy(self, request, *args, **kwargs):
        position = self.get_object()
        employees = position.employee_set.all()
        if employees:
            return Response(
                data='There are employees in this position. '
                     'Delete employees first to delete position',
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )

        return super().destroy(request)
