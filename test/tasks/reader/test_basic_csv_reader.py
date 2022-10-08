#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from io import StringIO
from unittest import TestCase

import pandas as pd

from src.tasks.reader import BasicCsvReader
from test.utils import TestConfigs


class TestBasicCsvReader(TestCase):

    def test_open(self):
        csv = "column_a,column_b\n" \
              "1,a\n" \
              "2,\n" \
              "3,c\n"

        def verify_data_in_file(csv_file):
            self.assertEqual(csv_file, "example.csv")
            return StringIO(csv)

        cfg = TestConfigs()
        cfg.path.data_in_file = verify_data_in_file

        reader = BasicCsvReader(cfg, "example")
        with reader.read() as chunks:
            for chunk in chunks:
                df = pd.DataFrame(chunk)
                break

        self.assertListEqual(df["column_a"].to_list(), ["1", "2", "3"])
        self.assertListEqual(df["column_b"].to_list(), ["a", "", "c"])

    def test_locate_csv_file(self):
        cfg = TestConfigs()
        cfg.path.data_in_file = lambda x: os.path.join("data_in", x)
        cfg.path.res_file = lambda x: os.path.join("res", x)

        reader = BasicCsvReader(cfg, "example", origin="data_in")
        self.assertEqual(reader.locate_csv_file(), "data_in/example.csv")

        reader = BasicCsvReader(cfg, "example", origin="res")
        self.assertEqual(reader.locate_csv_file(), "res/example.csv")

        reader = BasicCsvReader(cfg, "example", origin="blah")
        self.assertRaises(ValueError, reader.locate_csv_file)
