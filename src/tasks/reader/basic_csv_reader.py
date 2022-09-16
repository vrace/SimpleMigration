#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

from .basic_reader import BasicReader


class BasicCsvReader(BasicReader):

    def __init__(self, cfg, csv_name, chunk_size=1000):
        self.cfg = cfg
        self.csv_name = csv_name
        self.chunk_size = chunk_size

    def read(self):
        csv_file = self.cfg.path.data_in_file(f"{self.csv_name}.csv")
        return pd.read_csv(csv_file, dtype=str, na_filter=False, chunksize=self.chunk_size)
