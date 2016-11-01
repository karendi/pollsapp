from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.County)
admin.site.register(models.Constituency)
admin.site.register(models.Ward)
admin.site.register(models.President)
admin.site.register(models.Governor)
admin.site.register(models.Senator)
admin.site.register(models.Memberofparliament)
admin.site.register(models.Womensrep)
admin.site.register(models.MemberofCountyAssembly)
admin.site.register(models.Party)
admin.site.register(models.RallyDate)
