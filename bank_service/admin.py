from django.contrib import admin

from .models import Banks, Branches

admin.site.register((Banks, Branches))
