#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase

import pandas as pd

from src.tasks import BasicTask
from src.tasks.reader import BasicCsvReader
from src.tasks.writer import BasicSqlWriter
from test.utils import TestConfigs


class TestBasicTask(TestCase):

    def test_execute(self):
        def mock_reader_read():
            csv = "column_a,column_b\n" \
                  "a,1\n" \
                  "b,2\n" \
                  "c,3\n"
            return pd.read_csv(StringIO(csv), dtype=str, na_filter=False, chunksize=2)

        reader = BasicCsvReader("cfg", "example")
        reader.read = mock_reader_read

        write_iterator = 0

        def verify_writer_write(df, if_exists):
            nonlocal write_iterator
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

        cfg = TestConfigs()
        cfg.db.connect = lambda: "conn"
        writer = BasicSqlWriter(cfg, "example")
        writer.write = verify_writer_write

        task = BasicTask()
        task.create_reader = lambda: reader
        task.create_writer = lambda: writer

        task.execute()
        self.assertEqual(write_iterator, 2)
