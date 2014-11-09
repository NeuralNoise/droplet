from django.conf.urls import url, include
from rest_framework import routers
from droplet.rest.status.views import StatusViewSet
from droplet.rest.samba.views import DomainSettingsViewSet
from droplet.rest.catalog.views import ModuleInfoViewSet

router = routers.DefaultRouter()

router.register(r'status', StatusViewSet, base_name='status')
router.register(r'catalog/modules', ModuleInfoViewSet, base_name='catalog-modules')
router.register(r'samba/settings', DomainSettingsViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
