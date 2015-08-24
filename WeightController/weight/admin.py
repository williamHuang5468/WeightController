from django.contrib import admin

from .models import Weight

class WeightAdmin(admin.ModelAdmin):
	list_display = ('weight', 'record_date')

admin.site.register(Weight, WeightAdmin)
