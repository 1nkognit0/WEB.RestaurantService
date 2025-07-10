"""
ASGI config for cafeSaas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoprojec   t.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cafeSaas.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),

    }
)
