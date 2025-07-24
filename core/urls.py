from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import EventViewSet, RegistrationViewSet
from .views import EventViewSet, TestimonialViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'testimonials', TestimonialViewSet)

urlpatterns = router.urls

