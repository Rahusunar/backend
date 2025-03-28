from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import (
    HeroSection,
    AboutSection,
    ServiceSection,
    PortfolioSection,
    BlogsSection,
    ContactSection
)
from .serializers import (
    HeroSectionSerializer,
    AboutSectionSerializer,
    ServiceSectionSerializer,
    PortfolioSectionSerializer,
    BlogsSectionSerializer,
    ContactSectionSerializer
)

# Generic views for CRUD operations

class HeroSectionListCreateView(generics.ListCreateAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class HeroSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class AboutSectionListCreateView(generics.ListCreateAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class AboutSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer

class ServiceSectionListCreateView(generics.ListCreateAPIView):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer

class ServiceSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer

class PortfolioSectionListCreateView(generics.ListCreateAPIView):
    queryset = PortfolioSection.objects.all()
    serializer_class = PortfolioSectionSerializer

class PortfolioSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PortfolioSection.objects.all()
    serializer_class = PortfolioSectionSerializer

class BlogsSectionListCreateView(generics.ListCreateAPIView):
    queryset = BlogsSection.objects.all()
    serializer_class = BlogsSectionSerializer

class BlogsSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogsSection.objects.all()
    serializer_class = BlogsSectionSerializer

class ContactSectionListCreateView(generics.ListCreateAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer

class ContactSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer
