#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks import BasicTemplateTask
from test.utils import TestConfigs


class TestBasicTemplateTask(TestCase):

    def test_load_template(self):
        cfg = TestConfigs()
        task = BasicTemplateTask(cfg, "example")

        def mock_res_text(filename):
            self.assertEqual(filename, "example.template")
            return "the answer is {{ answer }}"

        cfg.path.res_text = mock_res_text

        template = task.load_template()
        text = template.render(answer=42)

        self.assertEqual(text, "the answer is 42")
