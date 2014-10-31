from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from droplet.web.menus import MenuItem


def menu(root):
    samba = MenuItem('samba', verbose_name=_('Samba'))

    samba.append(MenuItem('settings',
                            '/static/samba-settings.html',
                            verbose_name=_('Settings')))

    root.append(samba)
