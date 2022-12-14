#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .basic_task import BasicTask
from .reader import PSQLReader
from .writer import PSQLWriter


class BasicStagingTask(BasicTask):

    def __init__(self, cfg, staging_name):
        super().__init__(staging_name)
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg

    def create_reader(self):
        return PSQLReader(self.cfg, f"{self.name}_staging")

    def create_writer(self):
        return PSQLWriter(self.cfg, f"{self.name}_staging")

    def execute_begin(self):
        self.logger.info(f"Staging '{self.name}'")

    def execute_end(self, num_rows):
        self.logger.debug(f"...{num_rows} rows")

    def execute_transform_chunk(self, df):
        self.transform(df)

    def transform(self, df):
        self.logger.debug(f"{self.__class__.__name__}.transform() not implemented")
