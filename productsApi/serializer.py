from django.template.context_processors import request
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import authenticate
from .models import ProductModel

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price','description']


    def create(self, validated_data, *args, **kwargs):
        request = self.context.get('request')
        isAdmin = request.user.is_superuser or request.user.is_staff
        if isAdmin:
            product = ProductModel(
                name=validated_data['name'],
                price=validated_data['price']
            )
            product.save()
            return product
        else:
            raise serializers.ValidationError("Only staff users can create products.")