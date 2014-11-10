from rest_framework import viewsets
from rest_framework.response import Response
from droplet import common


class StatusViewSet(viewsets.ViewSet):
    """
    API endpoint that
    """
    def list(self, request):
        return Response({'changed': common.changed()})
