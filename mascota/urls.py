from django.conf.urls import url
from mascota.views import index

URL_PATTERNS = [
    url(r'^$', index),
]
