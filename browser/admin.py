from django.contrib import admin

from browser.models import Persos, CategoryContent


# classe utilizando o model do admin
class PersosContentAdmin(admin.ModelAdmin):
    # listar no display os seguintes campos
    list_display = ['id', 'title', 'sub_title', 'user', 'created']


# registrando models e configurando model na aplicação
admin.site.register(Persos, PersosContentAdmin)
admin.site.register(CategoryContent)
