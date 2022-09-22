#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src import MigrationApplicationSelector, MigrationApplication, MigrationExecuteTaskApplication
from test.utils import TestConfigs


class TestMigrationApplicationSelector(TestCase):

    def test_select_by_argv_with_empty_argv(self):
        cfg = TestConfigs()
        selector = MigrationApplicationSelector(cfg)
        app = selector.select_by_argv([])
        self.assertEqual(type(app), MigrationApplication)

    def test_select_by_argv_with_invalid_application(self):
        cfg = TestConfigs()
        selector = MigrationApplicationSelector(cfg)
        self.assertRaises(ValueError, selector.select_by_argv, ["xyz"])

    def test_select_with_args(self):
        cfg = TestConfigs()
        selector = MigrationApplicationSelector(cfg)

        app = selector.select_by_argv(["migrate"])
        self.assertEqual(type(app), MigrationApplication)

        app = selector.select_by_argv(["land", "abc", "def"])
        self.assertEqual(type(app), MigrationExecuteTaskApplication)
        self.assertEqual(app.task_type, "landing")
        self.assertEqual(app.task_names, ["abc", "def"])

        app = selector.select_by_argv(["stage", "ghi", "jkl"])
        self.assertEqual(type(app), MigrationExecuteTaskApplication)
        self.assertEqual(app.task_type, "staging")
        self.assertEqual(app.task_names, ["ghi", "jkl"])

        app = selector.select_by_argv(["consume", "mno", "pqr"])
        self.assertEqual(type(app), MigrationExecuteTaskApplication)
        self.assertEqual(app.task_type, "consumption")
        self.assertEqual(app.task_names, ["mno", "pqr"])
