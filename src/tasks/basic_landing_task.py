#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import pandas as pd

from .writer import BasicSqlWriter


class BasicLandingTask:

    def __init__(self, cfg, source, writer=None):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.source = source
        self.writer = writer or BasicSqlWriter(cfg.db)

    def execute(self):
        table_name = self.source.get_table_name()
        if_exists = "replace"
        self.logger.info(f"Landing '{table_name}'")
        num_rows = 0
        with self.source.open(self.cfg) as chunks:
            for chunk in chunks:
                df = pd.DataFrame(chunk)
                self.writer.write(df, table_name, if_exists)
                num_rows = num_rows + len(df)
                if if_exists == "replace":
                    if_exists = "append"
        self.logger.debug(f"...{num_rows} rows")
