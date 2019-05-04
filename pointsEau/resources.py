from tastypie.resources import ModelResource
from .models import PointEau

class PointEauResource(ModelResource):
    class Meta: 
        queryset = PointEau.objects.all()
        resource_name='points'
    
