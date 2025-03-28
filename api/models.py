from django.db import models

# Create your models here.
class HeroSection(models.Model):
    LogoImg = models.ImageField(upload_to='images/')
    HeroImg = models.ImageField(upload_to='images/HeroImg/')
    HeroTitle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.HeroTitle
    
class AboutSection(models.Model):
    PersonImg = models.ImageField(upload_to='images/MeetOurTeam/')
    NameOfPerson = models.CharField(max_length=100)
    PositionOfPerson = models.CharField(max_length=100)
    AboutPerson = models.TextField()
    Icon1 = models.CharField(max_length=100)
    Icon2 = models.CharField(max_length=100)
    Icon3 = models.CharField(max_length=100)
    SocialLink1 = models.URLField(max_length=300)
    SocialLink2 = models.URLField(max_length=300)
    SocialLink3 = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.NameOfPerson
class ServiceSection(models.Model):
    ServiceImg = models.ImageField(upload_to='images/Services/')
    ServiceTitle = models.CharField(max_length=100)
    ServiceTagLines = models.CharField(max_length=300)
    WhoDO = models.CharField(max_length=150)
    ServiceDescription = models.TextField()
    Feature1 = models.CharField(max_length=300)
    Feature2 = models.CharField(max_length=300)
    Feature3 = models.CharField(max_length=300)
    Feature4 = models.CharField(max_length=300)
    Feature5 = models.CharField(max_length=300, blank=True, null=True)
    Feature6 = models.CharField(max_length=300, blank=True, null=True)
    Feature7 = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.ServiceTitle
    
class PortfolioSection(models.Model):
    PortfolioImg = models.ImageField(upload_to='images/Portfolio/')
    PortfolioTitle = models.CharField(max_length=100)
    PortfolioLink = models.URLField(max_length=300)
    PortfolioDescription = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class BlogsSection(models.Model):
    BlogImg = models.ImageField(upload_to='images/Blogs/')
    BlogTitle = models.CharField(max_length=100)
    BlogDescription = models.TextField()
    BlogFaculty = models.CharField(max_length=100)
    BlogLink = models.URLField(max_length=300, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class ContactSection(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    
