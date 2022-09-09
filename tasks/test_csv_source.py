#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase

import pandas as pd

from tasks.csv_source import CsvSource


class TestCsvSource(TestCase):

    class DummyPathConfig:
        def data_in_file(self, csv):
            return StringIO(csv)

    class DummyConfig:
        def __init__(self, path):
            self.path = path

    def test_open(self):
        path_cfg = TestCsvSource.DummyPathConfig()
        cfg = TestCsvSource.DummyConfig(path_cfg)

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
