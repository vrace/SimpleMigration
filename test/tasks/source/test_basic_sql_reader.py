#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.tasks.reader import BasicSqlReader
from test.utils import TestConfigs


class TestBasicSqlReader(TestCase):

    def test_open(self):
        def verify_res_text(res_name):
            self.assertEqual(res_name, "example.sql")
            return "example query"

        cfg = TestConfigs()
        cfg.path.res_text = verify_res_text

        reader = BasicSqlReader(cfg, "example", chunk_size=200)
        with reader.read() as chunks:
            self.assertEqual(chunks.db_cfg, cfg.db)
            self.assertEqual(chunks.query, "example query")
            self.assertEqual(chunks.chunk_size, 200)
