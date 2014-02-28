__version__ = '0.1'
from django.db import settings
from django.db.models.signals import post_save

import importlib
import logging


def modules():
    """
    Return a list of instances of all present modules
    """
    from nazs.core.module import Module
    return [cls() for cls in Module.MODULES]


def conf_change(**kwargs):
    """
    Apply configuration changes on all the modules
    """
    logger = logging.getLogger(__name__)
    logger.info("Saving changes")
    return

    # Save + restart
    for module in modules():
        if module.enabled:
            logger.info("Saving module: %s" % module.name)
            module.save()
            module.restart()
        else:
            logger.info("Not saving disabled module: %s" % module.name)

    # Commit
    for module in modules():
        module.commit()

    logger.info("Changes saved")


def init():
    """
    Initialize nazs environment, setup logging, processes and all
    needed stuff for running nazs
    """
    from nazs.core.sudo import set_euid
    set_euid()

    # Load all modules
    for app in settings.INSTALLED_APPS:
        try:
            importlib.import_module(app + '.module')
        except:
            pass

    # DEVELOPMENT ONLY: save on model change
    for module in modules():
        for model in module.models():
            post_save.connect(conf_change, sender=model)
