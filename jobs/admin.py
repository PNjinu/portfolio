from django.contrib import admin
from .models import ContactMessages, Job, Blog

admin.site.register(Job)
admin.site.register(Blog)
admin.site.register(ContactMessages)
