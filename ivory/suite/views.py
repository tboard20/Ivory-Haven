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
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            date_in = request.POST.get('date_in')
            date_out = request.POST.get('date_out')
            adults = request.POST.get('adults')
            child = request.POST.get('child')
            message = request.POST.get('message')

            if not all([name, phone, email, date_in, date_out, adults, child]):
                return render(request, 'reservation.html', {'error': 'Please fill all required fields.'})

            email_body = f"""
Reservation Request:
Name: {name}
Phone: {phone}
Email: {email}
Check-in Date: {date_in}
Check-out Date: {date_out}
Adults: {adults}
Children: {child}
Message: {message or 'None'}
"""

            logger.info(f"Sending reservation email from {email} for {name}")
            send_mail(
                subject=f"Reservation Request from {name}",
                message=email_body,
                from_email=email,
                recipient_list=['tboad04@gmail.com'],
                fail_silently=False,
            )
            logger.info("Reservation email sent successfully")
            return render(request, 'reservation.html', {'success': True})

        except Exception as e:
            logger.error(f"Failed to send reservation email: {str(e)}")
            return render(request, 'reservation.html', {'error': str(e)})

    return render(request, 'reservation.html')