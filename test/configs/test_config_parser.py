#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

from src.configs.config_parser import ConfigParser


class TestConfigLoader(TestCase):

    def test_parse_value_with_none_value(self):
        self.assertIsNone(ConfigParser.parse(None))

    def test_parse_value_with_empty_value(self):
        self.assertEqual(ConfigParser.parse(""), "")

    def test_parse_value_with_escape(self):
        self.assertEqual(ConfigParser.parse("\\$funny"), "$funny")

    def test_parse_value_with_raw_text(self):
        self.assertEqual(ConfigParser.parse("answer"), "answer")

    @patch("os.getenv")
    def test_parse_value_with_env_name_only(self, getenv_fn):
        getenv_fn.return_value = "42"
        self.assertEqual(ConfigParser.parse("$answer"), "42")
        getenv_fn.assert_called_with("answer", default=None)

    @patch("os.getenv")
    def test_parse_value_with_env_name_and_default_value(self, getenv_fn):
        getenv_fn.return_value = "42"
        self.assertEqual(ConfigParser.parse("$answer:42"), "42")
        getenv_fn.assert_called_with("answer", default="42")
