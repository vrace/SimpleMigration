#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

from src import MigrationExecuteLandingApplication
from test.utils import TestConfigs
from test.utils import TestLandingTask


class TestRunLandingApplication(TestCase):

    def test_main(self):
        cfg = TestConfigs()
        task_abc = TestLandingTask(cfg, "abc")
        task_def = TestLandingTask(cfg, "def")

        app = MigrationExecuteLandingApplication(cfg, ["abc", "xyz"])
        app.collect_tasks = lambda: [task_abc]
        res = app.main()

        self.assertEqual(res, 0)
        self.assertTrue(task_abc.executed)
        self.assertFalse(task_def.executed)

    def test_main_with_exec_err(self):
        cfg = TestConfigs()
        task_abc = TestLandingTask(cfg, "abc")
        task_def = TestLandingTask(cfg, "def", True)

        app = MigrationExecuteLandingApplication(cfg, ["abc", "def"])
        app.collect_tasks = lambda: [task_abc, task_def]
        res = app.main()

        self.assertEqual(res, 1)
        self.assertTrue(task_abc.executed)
        self.assertTrue(task_def.executed)

    def test_execute_tasks(self):
        cfg = TestConfigs()
        task_abc = TestLandingTask(cfg, "abc")
        task_def = TestLandingTask(cfg, "def", True)
        task_ghi = TestLandingTask(cfg, "ghi", True)

        app = MigrationExecuteLandingApplication(cfg, [])
        num_errors = app.execute_tasks([task_abc, task_def, task_ghi])

        self.assertEqual(num_errors, 2)
        self.assertTrue(task_abc.executed)
        self.assertTrue(task_def.executed)
        self.assertTrue(task_ghi.executed)

    @patch("src.migration_execute_landing_application.collect_landing_tasks")
    def test_collect_tasks(self, mock_collect_landing_tasks):
        cfg = TestConfigs()
        task_abc = TestLandingTask(cfg, "abc")
        task_def = TestLandingTask(cfg, "def")
        task_ghi = TestLandingTask(cfg, "ghi")
        mock_collect_landing_tasks.return_value = [task_abc, task_def, task_ghi]

        app = MigrationExecuteLandingApplication(cfg, ["def"])
        tasks = app.collect_tasks()

        mock_collect_landing_tasks.assert_called_with(cfg)
        self.assertListEqual(tasks, [task_def])
