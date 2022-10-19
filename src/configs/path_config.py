#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

from .config_parser import ConfigParser


class PathConfig:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.data_in = ConfigParser.parse("$DATA_IN:data_in")
        self.data_out = ConfigParser.parse("$DATA_IN:data_out")
        self.res = "res"

    def data_in_file(self, filename):
        return os.path.join(self.data_in, filename)

    def data_out_file(self, filename):
        return os.path.join(self.data_out, filename)

    def res_file(self, filename):
        return os.path.join(self.res, filename)

    def res_text(self, filename):
        try:
            with open(self.res_file(filename)) as fp:
                return fp.read()
        except BaseException as exc:
            self.logger.error(f"Error loading resource {filename}")
            raise exc
