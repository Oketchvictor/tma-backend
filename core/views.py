from django.shortcuts import render
from rest_framework import viewsets
from .models import Registration
from .serializers import RegistrationSerializer
from .models import Event
from .serializers import EventSerializer
from .models import Testimonial
from .serializers import TestimonialSerializer




# Create your views here.
class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

