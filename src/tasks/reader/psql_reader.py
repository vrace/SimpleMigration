#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from contextlib import contextmanager

from .basic_csv_reader_chunks import BasicCsvReaderChunks
from .basic_reader import BasicReader


class PSQLReader(BasicReader):

    def __init__(self, cfg, query_name, db_cfg=None, chunk_size=1000):
        self.cfg = cfg
        self.query_name = query_name
        self.db_cfg = db_cfg or cfg.db
        self.chunk_size = chunk_size

    @contextmanager
    def read(self):
        csv_file = None
        try:
            csv_file = self.copy_to_csv()
            yield BasicCsvReaderChunks(csv_file, self.chunk_size)
        finally:
            if csv_file:
                os.remove(csv_file)

    def copy_to_csv(self):
        csv_file = self.cfg.path.data_out_file(f"{self.query_name}.tmp")
        raw_query = self.cfg.path.res_text(f"{self.query_name}.sql")
        conn = self.db_cfg.connect()
        raw_conn = conn.raw_connection()
        with raw_conn.cursor() as cursor, open(csv_file, "w") as fp:
            cursor.copy_expert(f"copy ({raw_query}) to stdout with csv header", fp)
        return csv_file
