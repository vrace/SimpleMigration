#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from tasks.writer import BasicSqlWriter


class TestBasicSqlWriter(TestCase):

    class DummyDBConfig:
        def connect(self):
            raise NotImplementedError()

    def test_write(self):
        db_cfg = TestBasicSqlWriter.DummyDBConfig()
        writer = BasicSqlWriter(db_cfg)

        self.assertRaises(NotImplementedError, writer.write, df="dummy", module_name="dummy", if_exists="dummy")
