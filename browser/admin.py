from django.contrib import admin

from browser.models import Persos, CategoryContent


class PersosContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sub_title', 'user', 'created']


admin.site.register(Persos, PersosContentAdmin)
admin.site.register(CategoryContent)
