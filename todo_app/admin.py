
from django.contrib import admin
from .models import TODO

class TodoAdmin(admin.ModelAdmin):
    list_display=('Title',)

admin.site.register(TODO,TodoAdmin)