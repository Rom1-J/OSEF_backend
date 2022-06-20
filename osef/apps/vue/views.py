from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.generic import View

VUE_TEMPLATE_PATH = "osef/templates/frontend"


class VueCSSView(View):
    template_name = "dist/css/"

    def get(self, request: WSGIRequest, path=""):
        file_path = settings.ROOT_DIR / VUE_TEMPLATE_PATH / self.template_name

        local_path = file_path / path

        if local_path.exists() and local_path.is_file():
            return HttpResponse(
                local_path.read_text(), content_type="text/css"
            )

        return HttpResponse(status=404)


class VueJSView(View):
    template_name = "dist/js/"

    def get(self, request: WSGIRequest, path=""):
        file_path = settings.ROOT_DIR / VUE_TEMPLATE_PATH / self.template_name

        local_path = file_path / path

        if local_path.exists() and local_path.is_file():
            return HttpResponse(
                local_path.read_text(), content_type="application/javascript"
            )

        return HttpResponse(status=404)


class VueImgView(View):
    template_name = "dist/img/"

    def get(self, request: WSGIRequest, path=""):
        file_path = settings.ROOT_DIR / VUE_TEMPLATE_PATH / self.template_name

        local_path = file_path / path
        ext = str(local_path).split(".")[-1]

        if local_path.exists() and local_path.is_file():
            if ext in ["svg", "png", "jpg", "jpeg"]:
                content_type = f"image/{ext}"

                return HttpResponse(
                    local_path.read_bytes(), content_type=content_type
                )

        return HttpResponse(status=404)


class VueFontsView(View):
    template_name = "dist/fonts/"

    def get(self, request: WSGIRequest, path=""):
        file_path = settings.ROOT_DIR / VUE_TEMPLATE_PATH / self.template_name

        local_path = file_path / path
        ext = str(local_path).split(".")[-1]

        if local_path.exists() and local_path.is_file():
            if ext in ["ttf", "oet", "woff"]:
                content_type = "application/octet-stream"

                return HttpResponse(
                    local_path.read_bytes(), content_type=content_type
                )

        return HttpResponse(status=404)
