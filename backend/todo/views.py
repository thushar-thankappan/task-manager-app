from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()
