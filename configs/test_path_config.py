#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from path_config import PathConfig


class PathConfigTest(TestCase):

    def test_data_in_file(self):
        filename = "data.txt"
        self.assertEqual(PathConfig.data_in_file(filename), "data_in/data.txt")

    def test_data_out_file(self):
        filename = "data.csv"
        self.assertEqual(PathConfig.data_out_file(filename), "data_out/data.csv")

    def test_res_file(self):
        filename = "staging.sql"
        self.assertEqual(PathConfig.res_file(filename), "res/staging.sql")
