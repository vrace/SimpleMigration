#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks.writer.basic_csv_writer import BasicCsvWriter
from test.utils import TestConfigs, TestDataFrame


class TestBasicCsvWriter(TestCase):

    def test_write(self):
        cfg = TestConfigs()
        cfg.path.data_out_file = lambda x: f"data_out/{x}"
        writer = BasicCsvWriter(cfg, "example")

        def verify_to_csv(csv_file, mode, header, index, float_format):
            self.assertEqual(csv_file, "data_out/example.csv")
            self.assertEqual(mode, "w")
            self.assertEqual(header, True)
            self.assertEqual(index, False)
            self.assertEqual(float_format, "%g")

        df = TestDataFrame()
        df.to_csv = verify_to_csv

        writer.write(df, "replace")

    def test_extract_write_args(self):
        cfg = TestConfigs()
        writer = BasicCsvWriter(cfg, "example")

        self.assertEqual(writer.extract_write_args("replace"), ("w", True))
        self.assertEqual(writer.extract_write_args("append"), ("a", False))
        self.assertRaises(ValueError, writer.extract_write_args, "meh")
