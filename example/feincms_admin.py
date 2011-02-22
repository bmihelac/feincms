from django.contrib.sites.admin import SiteAdmin

from feincms.admin import item_editor


class CMSSiteAdmin(SiteAdmin, item_editor.ItemEditor):
    pass

