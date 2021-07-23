from signature.models import Signatory
from django.contrib import admin
from .models import Signatory, Request

# Register your models here.
admin.site.register(Signatory)
admin.site.register(Request)