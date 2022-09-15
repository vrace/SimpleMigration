#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path

import pandas as pd


class CsvSource:

    def __init__(self, filename, chunksize=1000):
        self.filename = filename
        self.chunksize = chunksize

    def open(self, cfg):
        data_filename = cfg.path.data_in_file(self.filename)
        return pd.read_csv(data_filename, dtype=str, na_filter=False, chunksize=self.chunksize)

    def get_table_name(self):
        table_name, _ = os.path.splitext(self.filename)
        return table_name
