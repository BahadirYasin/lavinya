

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
    image = models.ImageField(upload_to='index_gallery/')
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

from django.db import models

class OrganizationService(models.Model):
    SERVICE_CHOICES = [
        ('salon', 'Salon Ücreti'),
        ('muzisyen', 'Müzisyen / Şantör'),
        ('fotografci', 'Fotoğrafçı'),
        ('qr', 'QR Kod Fotoğraf Paylaşımı'),
        ('kina', 'Kına Konsepti'),
        ('dugun', 'Düğün Konsepti'),
        ('araba', 'Araba Süsleme'),
        ('vip_arac', 'VIP Araç Hizmeti'),
        ('yemek_et', 'Yemek (Et)'),
        ('yemek_tavuk', 'Yemek (Tavuk)'),
        ('yemek_vegan', 'Yemek (Vegan)'),
        ('ikram_yas_pasta', 'Yaş Pasta'),
        ('ikram_kuru_pasta', 'Kuru Pasta'),
        ('ikram_cerez', 'Çerez'),
        ('ikram_mesrubat', 'Meşrubat'),
        ('ikram_cay', 'Çay'),
    ]
    key = models.CharField(max_length=32, choices=SERVICE_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_per_person = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.unit_price}₺{'/kişi' if self.is_per_person else ''})"


class WeddingOrganizationRequest(models.Model):
    date = models.DateField()
    guest_count = models.PositiveIntegerField(default=0)
    selected_services = models.JSONField()
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # İletişim bilgileri vs. ekleyebilirsin

    def __str__(self):
        return f"{self.date} - {self.guest_count} kişi"
    

    


    
