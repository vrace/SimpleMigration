#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase

import pandas as pd

from src.tasks import CsvSource
from src.tasks.basic_landing_task import BasicLandingTask
from src.tasks.writer import BasicSqlWriter
from test.utils import TestConfigs, TestDBConfig


class TestBasicLandingTask(TestCase):

    def test_init(self):
        cfg = "dummy cfg"
        source = "dummy source"
        writer = "dummy writer"

        task = BasicLandingTask(cfg, source, writer)

        self.assertEqual(task.cfg, cfg)
        self.assertEqual(task.source, source)
        self.assertEqual(task.writer, writer)

    def test_init_with_none_writer(self):
        cfg = TestConfigs()
        cfg.db = "dummy db cfg"
        source = "dummy source"

        task = BasicLandingTask(cfg, source)

        self.assertEqual(task.source, source)
        self.assertTrue(type(task.writer) == BasicSqlWriter)
        self.assertEqual(task.writer.db_cfg, "dummy db cfg")

    def test_execute(self):
        def mock_source_open(cfg):
            csv = "column_a,column_b\n" \
                  "a,1\n" \
                  "b,2\n" \
                  "c,3\n"
            return pd.read_csv(StringIO(csv), dtype=str, na_filter=False, chunksize=2)

        source = CsvSource("example.csv")
        source.open = mock_source_open

        write_iterator = 0

        def verify_writer_write(df, table_name, if_exists):
            nonlocal write_iterator
            self.assertEqual(table_name, "example")
            if write_iterator == 0:
                self.assertEqual(if_exists, "replace")
                self.assertListEqual(df["column_a"].to_list(), ["a", "b"])
                self.assertListEqual(df["column_b"].to_list(), ["1", "2"])
            elif write_iterator == 1:
                self.assertEqual(if_exists, "append")
                self.assertListEqual(df["column_a"].to_list(), ["c"])
                self.assertListEqual(df["column_b"].to_list(), ["3"])
            else:
                raise ValueError("test chunk not expected")
            write_iterator += 1

        writer = BasicSqlWriter(TestDBConfig())
        writer.write = verify_writer_write

        task = BasicLandingTask("dummy", source, writer)
        task.execute()
        self.assertEqual(write_iterator, 2)
