from rest_framework import viewsets
from .models import Division
from .serializers import DivisionSerializer
from rest_framework.response import Response
from rest_framework import status
from mptt.exceptions import InvalidMove


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.root_nodes()

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
