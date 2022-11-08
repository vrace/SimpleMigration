#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock

from src.tasks.writer.basic_csv_writer import BasicCsvWriter
from test.utils import TestConfigs, TestDataFrame


class TestBasicCsvWriter(TestCase):

    def test_write(self):
        cfg = TestConfigs()
        cfg.path.data_out_file = lambda x: f"data_out/{x}"
        writer = BasicCsvWriter(cfg, "example")

        df = TestDataFrame()
        df.to_csv = MagicMock()

        writer.write(df, "replace")
        df.to_csv.assert_called_with("data_out/example.csv", mode="w", header=True, index=False, float_format="%g")

    def test_extract_write_args(self):
        cfg = TestConfigs()
        writer = BasicCsvWriter(cfg, "example")

        self.assertEqual(writer.extract_write_args("replace"), ("w", True))
        self.assertEqual(writer.extract_write_args("append"), ("a", False))
        self.assertRaises(ValueError, writer.extract_write_args, "meh")
