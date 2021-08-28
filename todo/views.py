from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializers import ToDoSerializer, RegisterSerializer, TodoTextSerializer
from .models import ToDo, TodoText


class ToDoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title',
                        'description', ]


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username',
                        'email', ]


class ToDoTextView(viewsets.ModelViewSet):
    serializer_class = TodoTextSerializer
    queryset = TodoText.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username',
                        'email',
                        'text',
                        'status']

    # def total_task_count(self, request, *args, **kwargs):
    #     task_count = TodoText.objects.all().count()
    #     content = {'task_count': task_count}
    #     return content
