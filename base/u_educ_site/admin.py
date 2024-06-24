from django.contrib import admin
from .models import Role, SponsorPreferences, Mappings

# Register your models here.

admin.site.register(Role)
admin.site.register(SponsorPreferences)
admin.site.register(Mappings)