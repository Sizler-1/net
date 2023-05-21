from django.contrib import admin
from border.models import BorderCrossing, Vaccine, VaccineRecord

# Register your models here.

admin.site.register(BorderCrossing)
admin.site.register(Vaccine)
admin.site.register(VaccineRecord)