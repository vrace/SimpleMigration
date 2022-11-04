#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


class BasicCsvReaderChunks:

    def __init__(self, csv_file, chunk_size=1000):
        self.csv_file = csv_file
        self.chunk_size = chunk_size

    def __iter__(self):
        with pd.read_csv(self.csv_file, dtype=str, na_filter=False, chunksize=self.chunk_size) as chunks:
            for chunk in chunks:
                yield chunk
