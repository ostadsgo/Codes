from django.contrib import admin
from . import models


admin.site.register(models.Quote)
admin.site.register(models.Tag)