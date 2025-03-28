from rest_framework import serializers
from .models import (
    HeroSection,
    AboutSection,
    ServiceSection,
    PortfolioSection,
    BlogsSection,
    ContactSection
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'

class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = '__all__'

class PortfolioSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioSection
        fields = '__all__'

class BlogsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsSection
        fields = '__all__'

class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = '__all__'