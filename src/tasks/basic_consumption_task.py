#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .basic_task import BasicTask
from .reader import BasicSqlReader
from .writer import BasicCsvWriter


class BasicConsumptionTask(BasicTask):

    def __init__(self, cfg, consumption_name):
        super().__init__(consumption_name)
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.consumption_name = consumption_name

    def create_reader(self):
        return BasicSqlReader(self.cfg, f"{self.consumption_name}_consumption")

    def create_writer(self):
        return BasicCsvWriter(self.cfg, self.consumption_name)

    def execute_begin(self):
        self.logger.info(f"Consuming '{self.consumption_name}'")

    def execute_end(self, num_rows):
        self.logger.debug(f"...{num_rows} rows")
