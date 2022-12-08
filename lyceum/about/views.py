from django.views.generic import TemplateView


class DescriptionView(TemplateView):
    """View class for about page.

    render about page html.
    """
    template_name = 'about/index.html'
    extra_context = {'title': 'О проекте'}
