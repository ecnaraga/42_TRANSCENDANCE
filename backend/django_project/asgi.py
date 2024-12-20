import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from authent.authentication import JWTAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")


import chat.routing
import pong.routing

application = ProtocolTypeRouter({
    "http" :  get_asgi_application(),
	"websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            AuthMiddlewareStack(
                URLRouter(
                    pong.routing.websocket_urlpatterns + chat.routing.websocket_urlpatterns
                )
            )
        )
    ),
})
