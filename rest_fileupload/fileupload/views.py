from rest_framework.generics import (
    ListAPIView, CreateAPIView, ListCreateAPIView,
    # RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

)

from .models import Person
from .serializers import PersonSerializer


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
