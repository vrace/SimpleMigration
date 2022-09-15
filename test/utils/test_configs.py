#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestConfigs:
    def __init__(self):
        self.db = TestDBConfig()
        self.path = TestPathConfig()


class TestDBConfig:
    def __init__(self):
        self.connect = None


class TestPathConfig:
    def __init__(self):
        self.data_in_file = None
        self.data_out_file = None
        self.res_name = None
        self.res_text = None
