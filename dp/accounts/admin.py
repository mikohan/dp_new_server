from django.contrib import admin
from .models import BlackListEmail, Profile


admin.site.register(Profile)

admin.site.register(BlackListEmail)

# Register your models here.
