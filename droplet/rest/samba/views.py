from rest_framework import viewsets
from droplet.rest.samba.serializers import DomainSettingsSerializer
from droplet.samba.models import DomainSettings


class DomainSettingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that
    """
    queryset = DomainSettings.objects.all()
    serializer_class = DomainSettingsSerializer
