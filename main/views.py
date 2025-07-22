from django.shortcuts import render, redirect
from .models import Reservation
from .models import HeroSection
from .models import MenuSection
from .models import GalleryImage
from .models import IndexGallery
from django.core.mail import send_mail
from django.contrib import messages
from .models import CafeSection
import json
from django.shortcuts import render, redirect
from .models import OrganizationService, WeddingOrganizationRequest

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




def organization_request(request):
    services = OrganizationService.objects.all()
    services_json = json.dumps([
        {
            'key': s.key,
            'name': s.name,
            'unit_price': float(s.unit_price),
            'is_per_person': s.is_per_person
        } for s in services
    ])
    if request.method == 'POST':
        # Formdan gelen verileri işle
        date = request.POST.get('date')
        guest_count = int(request.POST.get('guest_count') or 0)
        selected_services = {}
        for s in services:
            if s.is_per_person:
                val = int(request.POST.get(s.key) or 0)
                if val > 0:
                    selected_services[s.key] = val
            else:
                if request.POST.get(s.key):
                    selected_services[s.key] = True
        detail = request.POST.get('detail', '')
        WeddingOrganizationRequest.objects.create(
            date=date,
            guest_count=guest_count,
            selected_services=selected_services,
            detail=detail
        )
        return redirect('organization_success')
    return render(request, 'organizations.html', {
        'services': services,
        'services_json': services_json
    })

def organization_success(request):
    return render(request, 'organization_success.html')





