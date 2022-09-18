#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks.basic_consumption_task import BasicConsumptionTask
from src.tasks.reader import BasicSqlReader
from test.utils import TestConfigs


class TestBasicConsumptionTask(TestCase):

    def test_create_reader(self):
        cfg = TestConfigs()
        task = BasicConsumptionTask(cfg, "example")
        reader = task.create_reader()
        self.assertEqual(type(reader), BasicSqlReader)
        self.assertEqual(reader.cfg, cfg)
        self.assertEqual(reader.query_name, "example_consumption")
