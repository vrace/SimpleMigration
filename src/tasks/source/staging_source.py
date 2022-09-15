#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import pandas as pd


class StagingSource:

    def __init__(self, cfg, staging_name, chunksize=1000):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.staging_name = staging_name
        self.chunksize = chunksize

    def open(self):
        query = self.load_staging_query()
        conn = self.cfg.db.connect()
        return pd.read_sql(query, conn, chunksize=self.chunksize)

    def load_staging_query(self):
        res_name = f"{self.staging_name}_staging.sql"
        return self.cfg.path.res_text(res_name)
