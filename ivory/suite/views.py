from django.shortcuts import render,redirect
from .models import ContactMessage
from .models import Reservation
from django.core.mail import send_mail
from django.conf import settings
import logging

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

logger = logging.getLogger(__name__)

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            logger.info(f"Sending email from {email} with message: {message}")
            send_mail(
                subject=f'Contact Form: {name}',
                message=message,
                from_email=email,
                recipient_list=['tboad04@gmail.com'],
                fail_silently=False,
            )
            logger.info("Email sent successfully")
            return render(request, 'contact.html', {'success': True})
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return render(request, 'contact.html', {'error': str(e)})
    return render(request, 'contact.html')
def events(request):
    return render(request, 'events.html')

def rooms(request):
    return render(request, 'rooms.html')



def reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date_in = request.POST.get('date_in')
        date_out = request.POST.get('date_out')
        adults = request.POST.get('adults')
        child = request.POST.get('child')
        message = request.POST.get('message')

        # Log form data for debugging
        logger.debug(f"Form data: name={name}, phone={phone}, email={email}, date_in={date_in}, date_out={date_out}, adults={adults}, child={child}, message={message}")

        # Check for missing fields
        missing_fields = []
        if not name:
            missing_fields.append('name')
        if not phone:
            missing_fields.append('phone')
        if not email:
            missing_fields.append('email')
        if not date_in:
            missing_fields.append('date_in')
        if not date_out:
            missing_fields.append('date_out')
        if not adults:
            missing_fields.append('adults')
        if not child:
            missing_fields.append('child')

        if missing_fields:
            logger.error(f"Missing fields: {', '.join(missing_fields)}")
            return render(request, 'reservation.html', {'error': f"Please fill all required fields: {', '.join(missing_fields)}"})

        email_content = f"Reservation:\nName: {name}\nPhone: {phone}\nEmail: {email}\nCheck-in: {date_in}\nCheck-out: {date_out}\nAdults: {adults}\nChildren: {child}\nNotes: {message or 'None'}"

        try:
            send_mail(
                subject=f"Reservation from {name}",
                message=email_content,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Use configured Gmail address
                recipient_list=['your-admin-email@example.com'],  # Replace with recipient email
                fail_silently=False,
            )
            return render(request, 'reservation.html', {'success': 'Reservation sent successfully!'})
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return render(request, 'reservation.html', {'error': 'Failed to send reservation. Please try again later.'})

    return render(request, 'reservation.html')