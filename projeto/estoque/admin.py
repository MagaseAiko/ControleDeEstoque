from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "criado_em", "editado_em"]