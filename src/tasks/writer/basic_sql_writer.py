#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .basic_writer import BasicWriter


class BasicSqlWriter(BasicWriter):

    def __init__(self, cfg, table_name, db_cfg=None):
        self.cfg = cfg
        self.table_name = table_name.lower()
        self.conn = (db_cfg or cfg.db).connect()

    def write(self, df, if_exists):
        df.to_sql(self.table_name, self.conn, if_exists=if_exists, index=False)
