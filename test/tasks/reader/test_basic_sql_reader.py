#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock

from src.tasks.reader import BasicSqlReader
from test.utils import TestConfigs


class TestBasicSqlReader(TestCase):

    def test_open(self):
        cfg = TestConfigs()
        cfg.path.res_text = MagicMock(return_value="example query")

        reader = BasicSqlReader(cfg, "example", chunk_size=200)
        with reader.read() as chunks:
            self.assertEqual(chunks.db_cfg, cfg.db)
            self.assertEqual(chunks.query, "example query")
            self.assertEqual(chunks.chunk_size, 200)

        cfg.path.res_text.assert_called_with("example.sql")
