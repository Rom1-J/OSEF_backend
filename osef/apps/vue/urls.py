from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import VueCSSView, VueImgView, VueJSView

app_name = "vue"
vue_template = TemplateView.as_view(template_name="frontend/dist/index.html")
urlpatterns = [
    # Blank urls
    path("login/", vue_template, name="account_login"),
    path("signup/", vue_template, name="account_signup"),
    path("invalid-email/", vue_template, name="account_invalid_email"),
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
        vue_template,
        name="home",
    ),
]
