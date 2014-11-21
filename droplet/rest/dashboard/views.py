from rest_framework import viewsets
from rest_framework.response import Response
from time import ctime
from socket import gethostname
from os import getloadavg


class DashboardViewSet(viewsets.ViewSet):
    """
    API endpoint that
    """
    def list(self, request):
        info = {}
        # FIXME: move this to some helper class outside the view?
        info['time'] = ctime()
        info['hostname'] = gethostname()
        info['version'] = '5.0 Technology Preview'
        info['load'] = ', '.join(map(str, getloadavg()))
        return Response(info)
