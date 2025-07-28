from django.contrib import admin
from .models import ContactMessage
from .models import Reservation


# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Reservation)