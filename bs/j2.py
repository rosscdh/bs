import os
import yaml
import base64

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', 'templates')

def b64encode_to_str(item):
    data = item.encode()
    return base64.b64encode(data).decode('utf-8')

class JinjaRenderer:
    """
    from service import JinjaRenderer
    jj = JinjaRenderer()
    rendered_string = jj.render(template_name='monkey.yml', name='andi')
    print(rendered_string)
    """
    env = None
    def __init__(self, templates_path='.'):
        self.env = Environment(
            loader=FileSystemLoader(set([TEMPLATES_PATH, templates_path])),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self.env.filters['bytesencode'] = str.encode
        self.env.filters['b64encode'] = b64encode_to_str
        self.env.filters['b64decode'] = base64.b64decode

        # try:
        #     secrets_yaml = self.env.get_template('encrypted/secrets.yml')
        #     self.secrets = yaml.load(secrets_yaml.render())
        # except:
        #     self.secrets = {'secrets'}

    def render(self, template_name, **kwargs):
        template = self.env.get_template(template_name)

        return template.render(**kwargs)