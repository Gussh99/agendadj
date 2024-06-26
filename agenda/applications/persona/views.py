from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import *
from rest_framework import generics
from .models import *
from .serializers import PersonPagination, PersonSerializer,PersonaSerializer,PersonaSerializer2, PersonaSerializer3,ReunionSerializer, ReunionSerializer2, ReunionSerializerLink, ReunionesByJobSerializer

class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    model = Person
    context_object_name = "personas"

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = 'persona/lista.html'

class PersonSearchApiView(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword 
        )
    
class PersonCreateView(generics.CreateAPIView):

    serializer_class = PersonSerializer

class PersonaDetailView(generics.RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonaDeleteView(generics.DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonaUpdateView(generics.UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonaRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonApiLIsta(generics.ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer2

    def get_queryset(self):
        queryset = Person.objects.all()
        return queryset


class ReunionApiLIsta(generics.ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = ReunionSerializer2

    def get_queryset(self):
        queryset = Reunion.objects.all()
        return queryset
    
class ReunionApiLIstaLink(generics.ListAPIView):
    #serializer_class = PersonaSerializer
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        queryset = Reunion.objects.all()
        return queryset

class PersonApiLIstaPagination(generics.ListAPIView):
    serializer_class = PersonaSerializer3
    pagination_class = PersonPagination

    def get_queryset(self):
        queryset = Person.objects.all()
        return queryset
    
class ReunionCountJob(generics.ListAPIView):
    serializer_class = ReunionesByJobSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()