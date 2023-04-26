from django.contrib import admin
from .models import Data, Contacts, Schedule, CallAnalytics

admin.site.register(Data)
admin.site.register(Contacts)
admin.site.register(Schedule)
admin.site.register(CallAnalytics)