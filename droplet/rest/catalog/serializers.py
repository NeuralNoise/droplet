from droplet.samba.models import DomainSettings
from rest_framework import serializers

class ModuleInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    url = serializers.CharField()

    def transform_name(self, obj, value):
        return obj.verbose_name
