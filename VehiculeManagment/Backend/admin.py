from django.contrib import admin

# Register your models here.

from Backend.models import Vehicule, FullTank, Intervention

admin.site.register(Vehicule)
admin.site.register(FullTank)
admin.site.register(Intervention)
