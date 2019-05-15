from rest_framework import routers
from . import views 
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'pointseau', PointEauViewSet, base_name='pointseau')
# urlpatterns = router.urls

urlpatterns = [
    path('pointseau/', views.PointsEauList.as_view()),
    path('pointseau/<int:pk>/', views.PointsEauDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)