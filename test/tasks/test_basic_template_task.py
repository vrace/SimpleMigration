#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock

from src.tasks import BasicTemplateTask
from test.utils import TestConfigs


class TestBasicTemplateTask(TestCase):

    def test_load_template(self):
        cfg = TestConfigs()
        cfg.path.res_text = MagicMock(return_value="the answer is {{ answer }}")

        task = BasicTemplateTask(cfg, "example")

        template = task.load_template()
        text = template.render(answer=42)

        self.assertEqual(text, "the answer is 42")
        cfg.path.res_text.assert_called_with("example.template")
