#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from .path_config import PathConfig


class PathConfigTest(TestCase):

    def test_data_in_file(self):
        filename = "data.txt"
        cfg = PathConfig()
        self.assertEqual(cfg.data_in_file(filename), "data_in/data.txt")

    def test_data_out_file(self):
        filename = "data.csv"
        cfg = PathConfig()
        self.assertEqual(cfg.data_out_file(filename), "data_out/data.csv")

    def test_res_file(self):
        filename = "staging.sql"
        cfg = PathConfig()
        self.assertEqual(cfg.res_file(filename), "res/staging.sql")
