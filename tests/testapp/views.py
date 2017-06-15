from django.views.generic import TemplateView


class PathIsTemplateNameQueryStringContextView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(
            PathIsTemplateNameQueryStringContextView, self).get_context_data(
                **kwargs)
        context.update(self.request.GET)
        return context

    def get_template_names(self):
        template_name = self.request.path
        if template_name.startswith('/'):
            template_name = template_name[1:]
        return template_name
