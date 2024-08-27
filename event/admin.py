from django.contrib import admin
from event.models import *

admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(Vendor)