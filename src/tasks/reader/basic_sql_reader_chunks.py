#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


class BasicSqlReaderChunks:

    def __init__(self, db_cfg, query, chunk_size=1000):
        self.db_cfg = db_cfg
        self.query = query
        self.chunk_size = chunk_size

    def __iter__(self):
        conn = self.db_cfg.connect()
        num_chunks = self.fetch_num_chunks(conn)
        for i in range(num_chunks):
            yield self.fetch_chunk(conn, i)

    def fetch_num_chunks(self, conn):
        count_query = f"select count(1) num_rows from ({self.query}) m"
        rs = conn.execute(count_query)
        xs = rs.fetchone()
        num_chunks = (int(xs["num_rows"]) + self.chunk_size - 1) // self.chunk_size
        rs.close()
        return num_chunks

    def fetch_chunk(self, conn, chunk_index):
        chunk_query = f"select * from ({self.query}) m limit {self.chunk_size} offset {self.chunk_size * chunk_index}"
        return pd.read_sql(chunk_query, conn)
