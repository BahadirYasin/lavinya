

# Create your models here.
from django.db import models


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
    background_image = models.ImageField(upload_to='hero/', verbose_name="Arka Plan Görseli")
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
    image = models.ImageField(upload_to='menu_items/')

    def __str__(self):
        return f"{self.name} ({self.section.title})"  

#GALERİ SAYFASINDAKİ RESİMLERİ DÜZENLEME EKLEME ÇIKARMA MODELİ  

class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Fotoğraf {self.pk}"
    

class IndexGallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='index_gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Index Görseli {self.id}"
    
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
    image = models.ImageField(upload_to='cafe_menu/')

    def __str__(self):
        return self.name

    


    
