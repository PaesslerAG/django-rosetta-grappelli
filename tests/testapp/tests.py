from django.conf import settings
from django.test import TestCase
from django.utils.six.moves.urllib.parse import urlencode


class RenderingBaseTemplateRegressionTestCase(TestCase):

    def test_can_render_the_base_template(self):
        content = self.get_rendered_base_template_with_following_context()
        self.assertNotIn(settings.TEMPLATE_STRING_IF_INVALID, content)

    def get_rendered_base_template_with_following_context(self, **kwargs):
        url = self.get_url()
        response = self.client.get(url)
        content = response.content.decode('utf8')
        return content

    def get_url(self, **kwargs):
        template_name = '/rosetta/base.html'
        query = self.get_querystring(**kwargs)
        url = '?'.join([template_name, query])
        return url

    def get_querystring(self, **kwargs):
        query_dict = dict(
            version='1.2.3',
            ADMIN_MEDIA_PREFIX='',
        )
        query_dict.update(kwargs)
        return urlencode(query_dict)
