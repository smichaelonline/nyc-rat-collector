from django.contrib import admin
from .models import Rat, Feeding, Trait

# Register your models here.
admin.site.register(Rat)
admin.site.register(Feeding)
admin.site.register(Trait)