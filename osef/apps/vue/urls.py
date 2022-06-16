from django.urls import re_path
from django.views.generic import TemplateView

from .views import VueCSSView, VueImgView, VueJSView

app_name = "vue"
urlpatterns = [
    re_path(
        r"^css/(?P<path>[a-zA-Z0-9/.~\-]+)$",
        VueCSSView.as_view(),
    ),
    re_path(
        r"^js/(?P<path>[a-zA-Z0-9/.~\-]+)$",
        VueJSView.as_view(),
    ),
    re_path(
        r"^img/(?P<path>[a-zA-Z0-9/.~\-]+)$",
        VueImgView.as_view(),
    ),
    re_path(
        "^.*$",
        TemplateView.as_view(template_name="dist/index.html"),
        name="home",
    ),
]
