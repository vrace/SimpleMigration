#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .configs import Configs
from .migration_db_config import MigrationDBConfig
from .path_config import PathConfig


class ConfigLoader:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load(self):
        self.logger.info("Initializing configs")
        return Configs(MigrationDBConfig(), PathConfig())
