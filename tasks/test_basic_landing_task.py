#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from unittest import TestCase

import pandas as pd

from tasks.basic_landing_task import BasicLandingTask
from tasks.writer import BasicSqlWriter


class TestBasicLandingTask(TestCase):

    def test_init(self):
        cfg = "dummy_cfg"
        source = "dummy_source"
        writer = "dummy_writer"

        task = BasicLandingTask(cfg, source, writer)

        self.assertEqual(task.cfg, cfg)
        self.assertEqual(task.source, source)
        self.assertEqual(task.writer, writer)

    def test_init_with_none_writer(self):
        class DummyConfig:
            def __init__(self):
                self.db = "dummy_db_cfg"

        cfg = DummyConfig()
        source = "dummy_source"

        task = BasicLandingTask(cfg, source)

        self.assertEqual(task.source, source)
        self.assertTrue(type(task.writer) == BasicSqlWriter)
        self.assertEqual(task.writer.db_cfg, "dummy_db_cfg")

    def test_execute(self):
        class DummySource:
            def open(self, cfg):
                csv = "column_a,column_b\n" \
                      "a,1\n" \
                      "b,2\n" \
                      "c,3\n"
                return pd.read_csv(StringIO(csv), dtype=str, na_filter=False, chunksize=2)

            def get_table_name(self):
                return "example"

        class DummyWriter:
            def __init__(self, ut):
                self.it = 0
                self.ut = ut

            def write(self, df, table_name, if_exists):
                self.ut.assertEqual(table_name, "example")
                if self.it == 0:
                    self.ut.assertEqual(if_exists, "replace")
                    self.ut.assertListEqual(df["column_a"].to_list(), ["a", "b"])
                    self.ut.assertListEqual(df["column_b"].to_list(), ["1", "2"])
                elif self.it == 1:
                    self.ut.assertEqual(if_exists, "append")
                    self.ut.assertListEqual(df["column_a"].to_list(), ["c"])
                    self.ut.assertListEqual(df["column_b"].to_list(), ["3"])
                else:
                    raise ValueError("test chunk not expected")
                self.it = self.it + 1

        writer = DummyWriter(self)
        task = BasicLandingTask("dummy", DummySource(), writer)
        task.execute()
        self.assertEqual(writer.it, 2)
