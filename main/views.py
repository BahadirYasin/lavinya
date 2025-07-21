from django.shortcuts import render, redirect
from .models import Reservation
from .models import HeroSection
from .models import MenuSection
from .models import GalleryImage
from .models import IndexGallery
from django.core.mail import send_mail
from django.contrib import messages
from .models import CafeSection
from .models import Organization

def index(request):
    hero_section = HeroSection.objects.all()
    gallery_images = IndexGallery.objects.all().order_by('-created_at')
    
    return render(request, 'index.html', {
        'hero_section': hero_section,
        'gallery_images': gallery_images,
    })


def menu_view(request):
    menu_sections = MenuSection.objects.prefetch_related('items').all()
    return render(request, 'menu.html', {'menu_sections': menu_sections})



def reservation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        detail = request.POST.get('detail', '')

        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            detail=detail
        )
        messages.success(request, "Rezervasyonunuz başarıyla gönderildi!")
        return redirect('reservation')  # form gönderildikten sonra aynı sayfaya dön
    return render(request, 'reservation.html')





def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject') or 'İletişim Formu'
        message = request.POST.get('message')

        full_message = f"""
        Yeni bir iletişim formu mesajı:

        Ad: {name}
        E-posta: {email}
        Telefon: {phone}
        Konu: {subject}
        Mesaj: {message}
        """

        send_mail(
            subject=f"📩 Lavinya Web İletişim: {subject}",
            message=full_message,
            from_email='webform@lavinya.com',  # Gönderici (tanımlı olmalı)
            recipient_list=['bahadir.cetinsoy2000@gmail.com'],  # ← Buraya kendi adresini yaz
            fail_silently=False,
        )

        messages.success(request, 'Mesajınız başarıyla gönderildi.')
        return redirect('contact')  # Sayfayı yenile

    return render(request, 'contact.html')


def organizations(request):
    return render(request, 'organizations.html')



def cafe_view(request):
    cafe_sections = CafeSection.objects.prefetch_related('items').all()
    return render(request, 'cafe.html', {'cafe_sections': cafe_sections})



def organization_view(request):
    if request.method == 'POST':
        data = request.POST
        org = Organization(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            date=data.get('date'),
            time=data.get('time'),
            salon_ucreti=data.get('salon_ucreti') or 0,
            muzisyen=bool(data.get('muzisyen')),
            fotografci=bool(data.get('fotografci')),
            qr_photo_sharing=bool(data.get('qr_photo_sharing')),
            kina_konsept=bool(data.get('kina_konsept')),
            dugun_konsept=bool(data.get('dugun_konsept')),
            ikram_yas_pasta=data.get('ikram_yas_pasta') or 0,
            ikram_kuru_pasta=data.get('ikram_kuru_pasta') or 0,
            ikram_cerez=data.get('ikram_cerez') or 0,
            ikram_mesrubat=data.get('ikram_mesrubat') or 0,
            ikram_cay=data.get('ikram_cay') or 0,
            yemek_var=bool(data.get('yemek_var')),
            yemek_kisi_sayisi=data.get('yemek_kisi_sayisi') or 0,
            yemek_aciklama=data.get('yemek_aciklama'),
            araba_susleme=bool(data.get('araba_susleme')),
            vip_arac=bool(data.get('vip_arac')),
            detail=data.get('detail'),
        )
        org.save()
        messages.success(request, 'Organizasyon başvurunuz alındı!')
        return redirect('organizations')
    return render(request, 'organizations.html')



