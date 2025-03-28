from django.urls import path
from .views import (
    HeroSectionListCreateView,
    HeroSectionDetailView,
    AboutSectionListCreateView,
    AboutSectionDetailView,
    ServiceSectionListCreateView,
    ServiceSectionDetailView,
    PortfolioSectionListCreateView,
    PortfolioSectionDetailView,
    BlogsSectionListCreateView,
    BlogsSectionDetailView,
    ContactSectionListCreateView,
    ContactSectionDetailView,
)

urlpatterns = [
    # HeroSection URLs
    path('hero/', HeroSectionListCreateView.as_view(), name='hero-list-create'),
    path('hero/<int:pk>/', HeroSectionDetailView.as_view(), name='hero-detail'),

    # AboutSection URLs
    path('about/', AboutSectionListCreateView.as_view(), name='about-list-create'),
    path('about/<int:pk>/', AboutSectionDetailView.as_view(), name='about-detail'),

    # ServiceSection URLs
    path('services/', ServiceSectionListCreateView.as_view(), name='services-list-create'),
    path('services/<int:pk>/', ServiceSectionDetailView.as_view(), name='services-detail'),

    # PortfolioSection URLs
    path('portfolio/', PortfolioSectionListCreateView.as_view(), name='portfolio-list-create'),
    path('portfolio/<int:pk>/', PortfolioSectionDetailView.as_view(), name='portfolio-detail'),

    # BlogsSection URLs
    path('blogs/', BlogsSectionListCreateView.as_view(), name='blogs-list-create'),
    path('blogs/<int:pk>/', BlogsSectionDetailView.as_view(), name='blogs-detail'),

    # ContactSection URLs
    path('contact/', ContactSectionListCreateView.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', ContactSectionDetailView.as_view(), name='contact-detail'),
]