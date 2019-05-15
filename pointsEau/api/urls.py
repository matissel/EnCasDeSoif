from rest_framework import routers
from . import views 
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register(r'pointseau', PointEauViewSet, base_name='pointseau')
# urlpatterns = router.urls

urlpatterns = [
    path('pointseau/', views.points_eau_list),
    path('pointseau/<int:pk>/', views.points_eau_detail),
]