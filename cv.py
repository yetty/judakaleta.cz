#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import yaml
import codecs
from jinja2 import Template

OUTPUTS = (
    ('template.html', 'index.html'),
)

if __name__ == '__main__':
    data = yaml.load(open('data.yaml'))

    for template, output_name in OUTPUTS:
        output = codecs.open(output_name, 'w', 'utf-8')
        template = Template(codecs.open(template, 'r', 'utf-8').read())
        output.write(template.render(**data))
