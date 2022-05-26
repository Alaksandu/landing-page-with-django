"""
WSGI config for fusion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# dj_static para carregar arquivos de mídia e estáticos no heroku
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')

#Usar o Cling e o MediaCling quando upar para o heroku na produção
application = Cling(MediaCling(get_wsgi_application()))
#application = get_wsgi_application()
