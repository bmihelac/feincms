from django.contrib import admin

from feincms.admin import editor

from example.models import Category, CMSSite, CMSSiteAdmin


class CategoryAdmin(editor.TreeEditor):
    list_display = ('name', 'slug')
    list_filter = ('parent',)
    prepopulated_fields = {
        'slug': ('name',),
        }


admin.site.register(Category, CategoryAdmin)
admin.site.register(CMSSite, CMSSiteAdmin)
