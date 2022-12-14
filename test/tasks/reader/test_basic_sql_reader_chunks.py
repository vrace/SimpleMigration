#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.tasks.reader import BasicSqlReaderChunks
from test.utils import TestConnection, TestResultSet


class TestBasicSqlReaderChunks(TestCase):

    def test_fetch_num_chunks(self):
        rs = TestResultSet()
        rs.fetchone = lambda: {"num_rows": 7}
        rs.close = lambda: None

        conn = TestConnection()
        conn.execute = MagicMock(return_value=rs)

        chunks = BasicSqlReaderChunks("dummy", "example", 2)
        self.assertEqual(chunks.fetch_num_chunks(conn), 4)
        conn.execute.assert_called_with("select count(1) num_rows from (example) m")

    def test_fetch_num_chunks_with_zero_rows(self):
        rs = TestResultSet()
        rs.fetchone = lambda: {"num_rows": 0}
        rs.close = lambda: None

        conn = TestConnection()
        conn.execute = MagicMock(return_value=rs)

        chunks = BasicSqlReaderChunks("dummy", "example", 2)
        self.assertEqual(chunks.fetch_num_chunks(conn), 1)
        conn.execute.assert_called_with("select count(1) num_rows from (example) m")

    @patch("pandas.read_sql")
    def test_fetch_chunk(self, mock_read_sql):
        chunks = BasicSqlReaderChunks("dummy", "example", 2)
        mock_read_sql.return_value = "example dataframe"
        self.assertEqual(chunks.fetch_chunk("conn", 2), "example dataframe")
        mock_read_sql.assert_called_with("select * from (example) m limit 2 offset 4", "conn")
