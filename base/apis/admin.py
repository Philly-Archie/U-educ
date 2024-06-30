from django.contrib import admin

# Register your models here.

from .models import UserModel, DetailsModel, FamEducationModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(DetailsModel)
admin.site.register(FamEducationModel)