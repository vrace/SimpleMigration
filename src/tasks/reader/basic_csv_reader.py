#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

from .basic_csv_reader_chunks import BasicCsvReaderChunks
from .basic_reader import BasicReader


class BasicCsvReader(BasicReader):

    def __init__(self, cfg, csv_name, chunk_size=1000, origin="data_in"):
        self.cfg = cfg
        self.csv_name = csv_name
        self.chunk_size = chunk_size
        self.origin = origin

    @contextmanager
    def read(self):
        try:
            csv_file = self.locate_csv_file()
            yield BasicCsvReaderChunks(csv_file, self.chunk_size)
        finally:
            pass

    def locate_csv_file(self):
        csv_filename = f"{self.csv_name}.csv"
        if self.origin == "data_in":
            return self.cfg.path.data_in_file(csv_filename)
        if self.origin == "res":
            return self.cfg.path.res_file(csv_filename)
        raise ValueError("origin can only be 'data_in' or 'res'")
