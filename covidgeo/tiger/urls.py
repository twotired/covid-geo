from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'states', views.StateViewSet)
router.register(r'counties', views.CountyViewSet)
router.register(r'urbanareas', views.UrbanAreaViewSet)
router.register(r'congressionaldistricts', views.CongressionalDistrictViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
