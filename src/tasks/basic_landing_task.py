#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .basic_task import BasicTask
from .reader import BasicCsvReader
from .writer import PSQLWriter


class BasicLandingTask(BasicTask):

    def __init__(self, cfg, table_name, origin="data_in"):
        super().__init__(table_name)
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.origin = origin

    def create_reader(self):
        return BasicCsvReader(self.cfg, self.name, origin=self.origin)

    def create_writer(self):
        return PSQLWriter(self.cfg, self.name)

    def execute_begin(self):
        self.logger.info(f"Landing '{self.name}'")

    def execute_end(self, num_rows):
        self.logger.debug(f"...{num_rows} rows")
