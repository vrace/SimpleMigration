#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

from .basic_reader import BasicReader
from .basic_sql_reader_chunks import BasicSqlReaderChunks


class BasicSqlReader(BasicReader):

    def __init__(self, cfg, query_name, db_cfg=None, chunk_size=1000):
        self.cfg = cfg
        self.query_name = query_name
        self.db_cfg = db_cfg or cfg.db
        self.chunk_size = chunk_size

    @contextmanager
    def read(self):
        try:
            query = self.load_query()
            chunks = BasicSqlReaderChunks(self.db_cfg, query, self.chunk_size)
            yield chunks
        finally:
            pass

    def load_query(self):
        res_name = f"{self.query_name}.sql"
        return self.cfg.path.res_text(res_name)
