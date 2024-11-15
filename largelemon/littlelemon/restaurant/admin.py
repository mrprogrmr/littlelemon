from django.contrib import admin
from .models import Booking, Menu

''' superuser credentials
## bistroadmin
## lemon@786!
## admin@littlelemon.com
'''

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)