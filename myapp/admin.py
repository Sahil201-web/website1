from django.contrib import admin
from .models import ButtonClick
# Register your models here.

class ButtonClickAdmin(admin.ModelAdmin):
    list_display = ('id', 'button_type', 'date_time', 'custom_id')

admin.site.register(ButtonClick,ButtonClickAdmin)    