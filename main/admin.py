from django.contrib import admin
from .models import Reservation
from .models import HeroSection
from .models import MenuSection, MenuItem
from .models import GalleryImage
from .models import IndexGallery
from .models import CafeSection, CafeItem


#REZERVASYON BİLGİLERİ
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone')

#HERO İÇİDENKİ BİLGİLER
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')

    def has_add_permission(self, request):
        # Sadece 1 adet HeroSection oluşturulmasına izin verir
        return not HeroSection.objects.exists()  


#MENU İÇİNDEKİ BÖLÜMLER VE MENÜ İTEMLERİ 
class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1

class MenuSectionAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(MenuSection, MenuSectionAdmin)


#GALERİDEKİ RESİMLER DEĞİŞTİRME 
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')

#INDEX SAYFASINDAKİ GALLERİYİ DEĞİŞTİRME
@admin.register(IndexGallery)
class IndexGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']


#KAFE MENUSU 
class CafeItemInline(admin.StackedInline):
    model = CafeItem
    extra = 1

class CafeSectionAdmin(admin.ModelAdmin):
    inlines = [CafeItemInline]

admin.site.register(CafeSection, CafeSectionAdmin)