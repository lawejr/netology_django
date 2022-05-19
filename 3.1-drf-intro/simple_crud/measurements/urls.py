from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('measurements', MeasurementViewSet, basename='measurements')

urlpatterns = router.urls
