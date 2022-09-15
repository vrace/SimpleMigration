#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch

from src.tasks.source.staging_source import StagingSource
from test.utils import TestConfigs


class TestStagingSource(TestCase):

    def test_load_staging_query(self):
        def verify_res_text(res_name):
            self.assertEqual(res_name, "example_staging.sql")
            return "example text"

        cfg = TestConfigs()
        cfg.path.res_text = verify_res_text

        source = StagingSource(cfg, "example")
        self.assertEqual(source.load_staging_query(), "example text")

    @patch("pandas.read_sql")
    def test_open(self, mock_read_sql):
        cfg = TestConfigs()
        cfg.db.connect = lambda: "dummy connection"
        cfg.path.res_text = lambda _: "example query"

        source = StagingSource(cfg, "example", 200)
        mock_read_sql.return_value = "example data"

        self.assertEqual(source.open(), "example data")
        mock_read_sql.assert_called_with("example query", "dummy connection", chunksize=200)
