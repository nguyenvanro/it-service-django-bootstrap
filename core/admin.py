from .models import Contact
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'description']
    search_fields = ('id',)
admin.site.register(Contact,ContactAdmin)
