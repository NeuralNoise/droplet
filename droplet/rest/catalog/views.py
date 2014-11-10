from rest_framework import viewsets
from rest_framework.response import Response
from droplet.rest.catalog.serializers import ModuleInfoSerializer
from droplet import common


class ModuleInfoViewSet(viewsets.ViewSet):
    """
    API endpoint that
    """
    def list(self, request):
        modules = common.modules()
        serializer = ModuleInfoSerializer(modules, many=True)
        return Response(serializer.data)
