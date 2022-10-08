#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks import BasicLandingTask
from src.tasks.reader import BasicCsvReader
from src.tasks.writer import BasicSqlWriter
from test.utils import TestConfigs


class TestBasicLandingTask(TestCase):

    def test_create_reader(self):
        task = BasicLandingTask("cfg", "example")
        reader = task.create_reader()
        self.assertEqual(type(reader), BasicCsvReader)
        self.assertEqual(reader.cfg, "cfg")
        self.assertEqual(reader.csv_name, "example")
        self.assertEqual(reader.origin, "data_in")

    def test_create_reader_with_origin_res(self):
        task = BasicLandingTask("cfg", "example", origin="res")
        reader = task.create_reader()
        self.assertEqual(type(reader), BasicCsvReader)
        self.assertEqual(reader.cfg, "cfg")
        self.assertEqual(reader.csv_name, "example")
        self.assertEqual(reader.origin, "res")

    def test_create_writer(self):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "conn"
        task = BasicLandingTask(cfg, "example")
        writer = task.create_writer()
        self.assertEqual(type(writer), BasicSqlWriter)
        self.assertEqual(writer.cfg, cfg)
        self.assertEqual(writer.table_name, "example")
