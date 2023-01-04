#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks.writer import PSQLWriter
from test.utils import TestConfigs


class TestPSQLWriter(TestCase):

    def test_psql_writer(self):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "dummy conn"
        writer = PSQLWriter(cfg, "DUMMY TABLE")

        self.assertEqual(writer.cfg, cfg)
        self.assertEqual(writer.table_name, "dummy table")
        self.assertEqual(writer.conn, "dummy conn")
