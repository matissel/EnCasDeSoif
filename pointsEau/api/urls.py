from .views import PointEauView
from django.urls.conf import path, re_path

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', PointEauView.as_view(), name="pointeau" )
]