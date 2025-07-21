

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

class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-posta")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    date = models.DateField(verbose_name="Tarih")
    time = models.TimeField(verbose_name="Saat")
    # Salon ve hizmetler
    salon_ucreti = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salon Ücreti")
    muzisyen = models.BooleanField(default=False, verbose_name="Müzisyen / Şantör")
    fotografci = models.BooleanField(default=False, verbose_name="Fotoğrafçı")
    qr_photo_sharing = models.BooleanField(default=False, verbose_name="QR Kod Fotoğraf Paylaşımı (Opsiyonel)")
    kina_konsept = models.BooleanField(default=False, verbose_name="Kına Konsepti")
    dugun_konsept = models.BooleanField(default=False, verbose_name="Düğün Konsepti")
    # İkram seçenekleri
    ikram_yas_pasta = models.PositiveIntegerField(verbose_name="Yaş Pasta (Kişi Başı)", default=0)
    ikram_kuru_pasta = models.PositiveIntegerField(verbose_name="Kuru Pasta (Kişi Başı)", default=0)
    ikram_cerez = models.PositiveIntegerField(verbose_name="Çerez (Kişi Başı)", default=0)
    ikram_mesrubat = models.PositiveIntegerField(verbose_name="Meşrubat (Kişi Başı)", default=0)
    ikram_cay = models.PositiveIntegerField(verbose_name="Çay (Kişi Başı)", default=0)
    # Yemek seçenekleri
    yemek_var = models.BooleanField(default=False, verbose_name="Yemek İstiyor musunuz?")
    yemek_kisi_sayisi = models.PositiveIntegerField(verbose_name="Yemek (Kişi Başı)", default=0)
    yemek_aciklama = models.TextField(blank=True, null=True, verbose_name="Yemek Seçenekleri Açıklama")
    # Araç hizmetleri
    araba_susleme = models.BooleanField(default=False, verbose_name="Araba Süsleme")
    vip_arac = models.BooleanField(default=False, verbose_name="Gün Boyu Şoförlü VIP Araç Hizmeti")
    # Ek bilgiler
    detail = models.TextField(blank=True, null=True, verbose_name="Ek Notlar")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    


    
