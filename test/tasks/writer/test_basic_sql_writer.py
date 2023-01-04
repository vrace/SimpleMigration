#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock

from src.tasks.writer import BasicSqlWriter
from test.utils import TestDataFrame, TestConfigs


class TestBasicSqlWriter(TestCase):

    def test_write(self):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "dummy conn"
        writer = BasicSqlWriter(cfg, "DUMMY TABLE")

        df = TestDataFrame()
        df.to_sql = MagicMock()

        writer.write(df, "replace")
        df.to_sql.assert_called_with("dummy table", "dummy conn", if_exists="replace", index=False)
