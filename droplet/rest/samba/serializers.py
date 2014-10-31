from droplet.samba.models import DomainSettings
from rest_framework import serializers


class DomainSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainSettings
        fields = ("mode", "domain", "workgroup", "realm", "netbios", "description")
