#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase
from unittest.mock import MagicMock

import pandas as pd

from src.tasks import BasicTask
from test.utils import TestConfigs


class WriterMock:

    def __init__(self, test_case):
        self.num_write = 0
        self.test_case = test_case

    def write(self, df, if_exists):
        if self.num_write == 0:
            self.test_case.assertEqual(if_exists, "replace")
            self.test_case.assertListEqual(df["column_a"].to_list(), ["a", "b"])
            self.test_case.assertListEqual(df["column_b"].to_list(), ["1", "2"])
        elif self.num_write == 1:
            self.test_case.assertEqual(if_exists, "append")
            self.test_case.assertListEqual(df["column_a"].to_list(), ["c"])
            self.test_case.assertListEqual(df["column_b"].to_list(), ["3"])
        else:
            raise ValueError("test chunk not expected")
        self.num_write += 1

    def verify(self):
        self.test_case.assertEqual(self.num_write, 2)


class TestBasicTask(TestCase):

    def test_execute(self):
        cfg = TestConfigs()
        cfg.db.connect = MagicMock(return_value="conn")

        csv = "column_a,column_b\n" \
              "a,1\n" \
              "b,2\n" \
              "c,3\n"

        reader = MagicMock()
        reader.read = MagicMock(return_value=pd.read_csv(StringIO(csv), dtype=str, na_filter=False, chunksize=2))

        writer = WriterMock(self)

        task = BasicTask("task")
        task.create_reader = lambda: reader
        task.create_writer = lambda: writer

        task.execute()
        writer.verify()
