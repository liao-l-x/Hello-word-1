"""
WSGI config for a01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
第一次改的地方
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a01.settings")
"""
靠靠靠
靠靠靠靠靠�,
"""
application = get_wsgi_application()
