from django.views.generic import TemplateView


class DescriptionView(TemplateView):
    template_name = 'about/index.html'
    extra_context = {'title': 'О проекте'}
