from django.contrib import admin
from .models import (
    HeroSection,
    AboutSection,
    ServiceSection,
    PortfolioSection,
    BlogsSection,
    ContactSection
)
# Register your models here.
admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(ServiceSection)
admin.site.register(PortfolioSection)
admin.site.register(BlogsSection)
admin.site.register(ContactSection)

