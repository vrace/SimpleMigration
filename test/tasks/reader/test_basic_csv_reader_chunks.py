#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from unittest import TestCase

import pandas as pd

from src.tasks.reader import BasicCsvReaderChunks


class TestBasicCsvReaderChunks(TestCase):

    def test_iter(self):
        csv = "ID,VALUE,_\n" \
              " 1,    A,\n" \
              " 2,    B,\n" \
              " 3,    C,\n"

        chunks = BasicCsvReaderChunks(StringIO(csv), chunk_size=2)
        num_chunks = 0
        for i, chunk in enumerate(chunks):
            num_chunks += 1
            df = pd.DataFrame(chunk)
            for it in df:
                df[it] = df[it].str.strip()
            if i == 0:
                self.assertListEqual(df["ID"].to_list(), ["1", "2"])
                self.assertListEqual(df["VALUE"].to_list(), ["A", "B"])
            elif i == 1:
                self.assertListEqual(df["ID"].to_list(), ["3"])
                self.assertListEqual(df["VALUE"].to_list(), ["C"])
        self.assertEqual(num_chunks, 2)
