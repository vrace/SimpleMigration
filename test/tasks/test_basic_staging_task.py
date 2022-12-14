#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks import BasicStagingTask
from src.tasks.reader import PSQLReader
from src.tasks.writer import PSQLWriter
from test.utils import TestConfigs


class TestBasicStagingTask(TestCase):

    def test_create_reader(self):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "conn"
        task = BasicStagingTask(cfg, "example")
        reader = task.create_reader()
        self.assertEqual(type(reader), PSQLReader)
        self.assertEqual(reader.cfg, cfg)
        self.assertEqual(reader.query_name, "example_staging")

    def test_create_writer(self):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "conn"
        task = BasicStagingTask(cfg, "example")
        writer = task.create_writer()
        self.assertEqual(type(writer), PSQLWriter)
        self.assertEqual(writer.cfg, cfg)
        self.assertEqual(writer.table_name, "example_staging")
