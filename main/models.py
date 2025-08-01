

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField


#REZERVASYON FORMU MODELİ

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    detail = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
    
#ANASAYFADAKİ HERO, RESMİ VE AÇIKLAMASI DEĞİŞTİRME MODELİ

class HeroSection(models.Model):
    background_image = CloudinaryField('image')
    title = models.CharField(max_length=100, verbose_name="Başlık")
    subtitle = models.CharField(max_length=200, verbose_name="Alt Başlık")
    button_text = models.CharField(max_length=50, verbose_name="Buton Yazısı")
    button_link = models.CharField(max_length=200, verbose_name="Buton Linki")

    def __str__(self):
        return self.title
    
#MENU İÇİNDEKİ BÖLÜM VE İTEMLERİ DEĞİŞTİRME MODELİ 
    
class MenuSection(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField("İçindekiler", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image =  CloudinaryField('image')

    def __str__(self):
        section_title = getattr(self.section, "title", "")
        return f"{self.name} ({section_title})"  

#GALERİ SAYFASINDAKİ RESİMLERİ DÜZENLEME EKLEME ÇIKARMA MODELİ  

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Fotoğraf {self.pk}"
    

class IndexGallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Index Görseli {getattr(self, 'id', '')}"
    
from django.db import models

class CafeSection(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CafeItem(models.Model):
    section = models.ForeignKey(CafeSection, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image =  CloudinaryField('image')

    def __str__(self):
        return self.name

from cloudinary.models import CloudinaryField

class OrganizationCard(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify

class CalendarDay(models.Model):
    date = models.DateField(unique=True)
    is_available = models.BooleanField(default=True)  # True: Boş, False: Dolu

    def __str__(self):
        return f"{self.date} - {'Boş' if self.is_available else 'Dolu'}"

class OrganizationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    image = CloudinaryField('image', blank=True, null=True)  # İstersen görsel de ekle
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class ServiceOption(models.Model):
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField()
    per_person = models.BooleanField(default=False)
    # diğer alanlar...

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.organization_type})"

        





    


    
