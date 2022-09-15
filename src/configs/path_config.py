#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class PathConfig:

    def __init__(self):
        self.data_in = "data_in"
        self.data_out = "data_out"
        self.res = "res"

    def data_in_file(self, filename):
        return os.path.join(self.data_in, filename)

    def data_out_file(self, filename):
        return os.path.join(self.data_out, filename)

    def res_file(self, filename):
        return os.path.join(self.res, filename)
