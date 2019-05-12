from rest_framework import routers
from .views import PointEauViewSet, AdminPointEauView
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pointseau', PointEauViewSet, base_name='pointseau')
router.register(r'pointseauadmin', AdminPointEauView, base_name="pointseauadmin")
urlpatterns = router.urls