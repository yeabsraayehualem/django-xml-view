pip install django-xml-view

## Usage

1. Add `xml_renderer` to your `INSTALLED_APPS` in `settings.py`:

    ```python
    INSTALLED_APPS = [
        # Other apps
        'xml_renderer',
    ]
    ```

2. Use the `render_xml` function in your views:

    ```python
    from xml_renderer.xmlrenderer import render_xml

    def home(req):
        xslt_url = static('style.xsl')
        return render_xml(req, "home.xml", {'xslt': xslt_url})
    ```

## License

This project is licensed under the MIT License.
