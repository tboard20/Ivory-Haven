from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def rooms(request):
    return render(request, 'rooms.html')


def reservation(request):
    return render(request, 'reservation.html')