from .models import *
from rest_framework import serializers


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=RestaurantModel
        fields=('id','name','valuation','address')