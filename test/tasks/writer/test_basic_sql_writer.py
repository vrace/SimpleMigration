#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks.writer import BasicSqlWriter
from test.utils import TestDBConfig, TestDataFrame


class TestBasicSqlWriter(TestCase):

    def test_write(self):
        db_cfg = TestDBConfig()
        db_cfg.connect = lambda: "dummy conn"
        writer = BasicSqlWriter(db_cfg)

        def verify_to_sql(table_name, conn, if_exists, index):
            self.assertEqual(table_name, "dummy table")
            self.assertEqual(conn, "dummy conn")
            self.assertEqual(if_exists, "replace")
            self.assertFalse(index)

        df = TestDataFrame()
        df.to_sql = verify_to_sql

        writer.write(df, "dummy table", "replace")
