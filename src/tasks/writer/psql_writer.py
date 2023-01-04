#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from io import StringIO

from .basic_writer import BasicWriter


class PSQLWriter(BasicWriter):

    def __init__(self, cfg, table_name, db_cfg=None):
        self.cfg = cfg
        self.table_name = table_name.lower()
        self.conn = (db_cfg or cfg.db).connect()

    def write(self, df, if_exists):
        if if_exists == "replace":
            df[:0].to_sql(self.table_name, self.conn, if_exists="replace", index=False)
        buf = StringIO()
        df.to_csv(buf, index=False, header=False, float_format="%g", quoting=csv.QUOTE_NONE, escapechar='\\')
        buf.seek(0)
        raw_conn = self.conn.raw_connection()
        with raw_conn.cursor() as cursor:
            cursor.copy_from(buf, self.table_name, sep=',', null='')
        raw_conn.commit()
