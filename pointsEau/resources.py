from tastypie.resources import ModelResource
from .models import PointEau
from tastypie.authorization import Authorization

class PointEauResource(ModelResource):
    class Meta: 
        queryset = PointEau.objects.all()
        resource_name='points'
        authorization = Authorization()    
