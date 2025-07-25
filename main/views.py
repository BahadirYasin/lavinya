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
from django.shortcuts import render
from .models import ServiceOption
from django.shortcuts import render
from .models import ServiceOption, OrganizationType
from .models import OrganizationCard
from .models import OrganizationCard, CalendarDay
import json
from django.core.serializers.json import DjangoJSONEncoder


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



def cafe_view(request):
    cafe_sections = CafeSection.objects.prefetch_related('items').all()
    return render(request, 'cafe.html', {'cafe_sections': cafe_sections})



def organizations_view(request):
    org_types = OrganizationType.objects.all()
    services = ServiceOption.objects.all()
    org_cards = OrganizationCard.objects.all()
    calendar_days = CalendarDay.objects.all()
    calendar_days_json = json.dumps(
        [
            {"date": str(day.date), "is_available": day.is_available}
            for day in calendar_days
        ],
        cls=DjangoJSONEncoder
    )

    context = {
        'org_choices': org_types,
        'service_options': list(services.values(
            'id', 'organization_type', 'category', 'name', 'slug', 'price', 'per_person', 
            'organization_type__slug', 'category__slug', 'category__name'
        )),
        'org_cards': org_cards,
        'calendar_days': calendar_days,
        'calendar_days_json': calendar_days_json,  # <-- Bunu ekledik!
    }
    return render(request, 'organizations.html', context)
















