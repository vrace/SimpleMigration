#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

from src import MigrationExecuteTaskApplication
from test.utils import TestConfigs
from test.utils import TestTask


class TestMigrationExecuteTaskApplication(TestCase):

    def test_main(self):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")

        app = MigrationExecuteTaskApplication(cfg, "landing", ["abc", "xyz"])
        app.collect_tasks = lambda: [task_abc]
        res = app.main()

        self.assertEqual(res, 0)
        self.assertTrue(task_abc.executed)
        self.assertFalse(task_def.executed)

    def test_main_with_exec_err(self):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def", True)

        app = MigrationExecuteTaskApplication(cfg, "landing", ["abc", "def"])
        app.collect_tasks = lambda: [task_abc, task_def]
        res = app.main()

        self.assertEqual(res, 1)
        self.assertTrue(task_abc.executed)
        self.assertTrue(task_def.executed)

    def test_execute_tasks(self):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def", True)
        task_ghi = TestTask(cfg, "ghi", True)

        app = MigrationExecuteTaskApplication(cfg, "landing", [])
        num_errors = app.execute_tasks([task_abc, task_def, task_ghi])

        self.assertEqual(num_errors, 2)
        self.assertTrue(task_abc.executed)
        self.assertTrue(task_def.executed)
        self.assertTrue(task_ghi.executed)

    @patch("src.migration_execute_task_application.collect_landing_tasks")
    def test_collect_tasks_landing(self, mock_collect_landing_tasks):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")
        task_ghi = TestTask(cfg, "ghi")
        mock_collect_landing_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteTaskApplication(cfg, "landing", ["def"])
        tasks = app.collect_tasks()

        mock_collect_landing_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_def])

    @patch("src.migration_execute_task_application.collect_staging_tasks")
    def test_collect_tasks_staging(self, mock_collect_staging_tasks):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")
        task_ghi = TestTask(cfg, "ghi")
        mock_collect_staging_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteTaskApplication(cfg, "staging", ["abc"])
        tasks = app.collect_tasks()

        mock_collect_staging_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_abc])

    @patch("src.migration_execute_task_application.collect_consumption_tasks")
    def test_collect_tasks_consumption(self, mock_collect_consumption_tasks):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")
        task_ghi = TestTask(cfg, "ghi")
        mock_collect_consumption_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteTaskApplication(cfg, "consumption", ["ghi"])
        tasks = app.collect_tasks()

        mock_collect_consumption_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_ghi])

    @patch("src.migration_execute_task_application.collect_misc_tasks")
    def test_collect_tasks_misc(self, mock_collect_misc_tasks):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")
        task_ghi = TestTask(cfg, "ghi")
        mock_collect_misc_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteTaskApplication(cfg, "misc", ["abc", "def"])
        tasks = app.collect_tasks()

        mock_collect_misc_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_abc, task_def])

    @patch("src.migration_execute_task_application.collect_landing_tasks")
    def test_collect_tasks_without_names(self, mock_collect_landing_tasks):
        cfg = TestConfigs()
        task_abc = TestTask(cfg, "abc")
        task_def = TestTask(cfg, "def")
        task_ghi = TestTask(cfg, "ghi")
        mock_collect_landing_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteTaskApplication(cfg, "landing", [])
        tasks = app.collect_tasks()

        mock_collect_landing_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_abc, task_def, task_ghi])
