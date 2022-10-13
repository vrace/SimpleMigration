#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jinja2 import BaseLoader, Environment

from .basic_misc_task import BasicMiscTask


class BasicTemplateTask(BasicMiscTask):

    def __init__(self, cfg, name):
        self.cfg = cfg
        super().__init__(name)

    def template_name(self):
        return f"{self.name}.template"

    def template_args(self):
        return {}

    def render_output_name(self):
        return self.name

    def load_template(self):
        template_text = self.cfg.path.res_text(self.template_name())
        return Environment(loader=BaseLoader()).from_string(template_text)

    def render_template(self, template):
        text = template.render(**self.template_args())
        with open(self.cfg.path.data_out_file(self.render_output_name()), "w") as fp:
            fp.write(text)
            fp.write("\n")

    def execute(self):
        template = self.load_template()
        self.render_template(template)
