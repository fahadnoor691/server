from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.cache import cache_page

# Create your views here.
@api_view(['POST'])
def create_user(request):
    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_users(request):
    users = UserDetails.objects.all()
    serializer = UserDetailsSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def update_user(request, pk):
    if request.method == 'PUT':
        user = UserDetails.objects.get(id=pk)
        serializer = UserDetailsSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user = UserDetails.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_user(request, pk):
    try:
        user = UserDetails.objects.get(id=pk)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
    except UserDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)