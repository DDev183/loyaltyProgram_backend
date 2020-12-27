from django.contrib import admin

# Register your models here.
from restApp.quickstart import models

admin.site.register(models.Card)
admin.site.register(models.Log)
admin.site.register(models.userProfile)

