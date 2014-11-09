from rest_framework import viewsets
from droplet.rest.samba.serializers import DomainSettingsSerializer
from droplet.samba.models import DomainSettings
from rest_framework.response import Response

class DomainSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that
    """
    queryset = DomainSettings.objects.all()
    serializer_class = DomainSettingsSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=422)
        serializer.save()
        return Response()
