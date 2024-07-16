from rest_framework import serializers
from .models import *
from django.db.models import *


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'
        