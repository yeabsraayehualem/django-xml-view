# xml_renderer_app/xml_renderer.py

from django.template import loader
from django.http import HttpResponse

def render_xml(request, template_name, context={}):
    """Render an XML response based on the given template and context."""
    template = loader.get_template(template_name)
    xml_content = template.render(context, request)

    return HttpResponse(xml_content, content_type='application/xml')
