#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase

import pandas as pd

from src.tasks.source import CsvSource


class TestCsvSource(TestCase):

    def test_open(self):
        class DummyPathConfig:
            def data_in_file(self, csv):
                return StringIO(csv)

        class DummyConfig:
            def __init__(self, path):
                self.path = path

        path_cfg = DummyPathConfig()
        cfg = DummyConfig(path_cfg)

        csv = "column_a,column_b\n" \
              "1,a\n" \
              "2,\n" \
              "3,c\n"

        source = CsvSource(csv)
        with source.open(cfg) as chunks:
            for chunk in chunks:
                df = pd.DataFrame(chunk)
                break

        self.assertListEqual(df["column_a"].to_list(), ["1", "2", "3"])
        self.assertListEqual(df["column_b"].to_list(), ["a", "", "c"])

    def test_get_table_name(self):
        source = CsvSource("sample_data.csv")
        self.assertEqual(source.get_table_name(), "sample_data")
