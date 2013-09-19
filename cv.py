#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import yaml
import codecs
from jinja2 import Template

if __name__ == '__main__':
    output = codecs.open('index.html', 'w', 'utf-8')
    template = Template(codecs.open('template.html', 'r', 'utf-8').read())
    data = yaml.load(open('data.yaml'))
    output.write(template.render(**data))
