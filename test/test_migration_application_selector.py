#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src import MigrationApplicationSelector, MigrationApplication
from test.utils import TestConfigs


class TestMigrationApplicationSelector(TestCase):

    def test_select_by_argv_with_empty_argv(self):
        cfg = TestConfigs()
        selector = MigrationApplicationSelector(cfg)
        app = selector.select_by_argv([])
        self.assertEqual(type(app), MigrationApplication)

    def test_select_by_argv_with_invalid_application(self):
        cfg = TestConfigs()
        selectors = MigrationApplicationSelector(cfg)
        self.assertRaises(ValueError, selectors.select_by_argv, ["xyz"])
