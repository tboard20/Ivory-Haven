from django.shortcuts import render,redirect
from .models import ContactMessage
from .models import Reservation
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        contact_message = ContactMessage(
            name = name,
            email = email,
            phone = phone,
            message = message,
        )

        contact_message.save()

        try:
            send_mail(
                subject = "Ivory Haven",
                message = f"From: {name} ({email}) \n\nmessage \n{message}",
                from_email= settings.DEFAULT_FROM_EMAIL,
                recipient_list=['tboad04@gmail.com'],
                fail_silently=False,
            )

        except Exception as e:
            print(f"email sending failed: {e}")
            return redirect("contact")

    
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def rooms(request):
    return render(request, 'rooms.html')


def reservation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        note = request.POST.get('note')
        date_in = request.POST.get('date_in')
        date_out = request.POST.get('date_out')
        adult = request.POST.get('adult')
        child = request.POST.get('child')


        reserve = Reservation(
            name = name,
            email = email,
            phone = phone,
            note = note,
            date_in = date_in,
            date_out = date_out,
            child = child,
            adult = adult,
        )

        reserve.save()

        try:
            send_mail(
                subject = "Ivory Haven",
                message = f"From: {name} ({email}) \n\note \n{note}",
                from_email= settings.DEFAULT_FROM_EMAIL,
                recipient_list=['tboad04@gmail.com'],
                fail_silently=False,
            )

        except Exception as e:
            print(f"email sending failed: {e}")
            return redirect("reservation")


    return render(request, 'reservation.html')