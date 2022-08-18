#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class PathConfig:

    data_in = "data_in"
    data_out = "data_out"
    res = "res"

    @staticmethod
    def data_in_file(filename):
        return os.path.join(PathConfig.data_in, filename)

    @staticmethod
    def data_out_file(filename):
        return os.path.join(PathConfig.data_out, filename)

    @staticmethod
    def res_file(filename):
        return os.path.join(PathConfig.res, filename)
