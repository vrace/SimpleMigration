#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .basic_task import BasicTask
from .reader import BasicCsvReader
from .writer import BasicSqlWriter


class BasicLandingTask(BasicTask):

    def __init__(self, cfg, table_name):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.table_name = table_name

    def create_reader(self):
        return BasicCsvReader(self.cfg, self.table_name)

    def create_writer(self):
        return BasicSqlWriter(self.cfg, self.table_name)

    def execute_begin(self):
        self.logger.info(f"Landing '{self.table_name}'")

    def execute_end(self, num_rows):
        self.logger.debug(f"...{num_rows} rows")
