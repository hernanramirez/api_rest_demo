from django.views.generic import TemplateView


class FrontendView(TemplateView):
    # group_required = u"Administradores"
    template_name = "frontend/frontend.html"
