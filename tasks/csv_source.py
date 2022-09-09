#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


class CsvSource:

    def __init__(self, filename):
        self.filename = filename

    def open(self, cfg):
        data_filename = cfg.path.data_in_file(self.filename)
        return pd.read_csv(data_filename, dtype=str, na_filter=False, chunksize=1000)
