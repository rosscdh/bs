import os
import json
import yaml
import click
import pprint
import logging

from bs.j2 import JinjaRenderer

logging.basicConfig(filename='bs.log',level=logging.DEBUG)

LEVEL = os.getenv('LOGLEVEL', 'INFO')

logger = logging.getLogger()
logger.setLevel(getattr(logging, LEVEL))


@click.command()
@click.option('--filename', '-f', required=True, multiple=False, help='The yml file to apply the parameters to')
@click.option('--parameter', '-p', required=True, multiple=True, help='The parameter KEY=value')
@click.option('--output', '-o', required=False, multiple=False, help='the output json file')
def bs(filename, parameter, output):
    """oc process replacement tool
    Will take a template.yml
    take parameters in KEY=VALUE format
    and allow you to use Jinja2 in your template.yml
    """
    context = dict([item.split('=') for item in parameter])

    jj = JinjaRenderer()
    rendered_string = jj.render(template_name=filename, **context)
    data = yaml.load(rendered_string)

    logger.info(rendered_string)
    logger.info('-------' * 10)

    pprint.pprint(data)

    if output:
        with open(output, 'w') as output_file:
            json.dump(data, output_file)


if __name__ == '__main__':
    bs()