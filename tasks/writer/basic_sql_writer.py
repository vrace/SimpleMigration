#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BasicSqlWriter:

    def __init__(self, db_cfg):
        self.db_cfg = db_cfg

    def write(self, df, module_name, if_exists):
        conn = self.db_cfg.connect()
        df.to_sql(module_name, conn, if_exists=if_exists, index=False)
