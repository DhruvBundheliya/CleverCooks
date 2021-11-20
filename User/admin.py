from django.contrib import admin
from .models import Verification

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ['id','user','token','verify']
