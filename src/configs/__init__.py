#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from .configs import Configs
from .logging_config import init_logging
from .migration_db_config import MigrationDBConfig
from .path_config import PathConfig


def init_configs():
    init_logging()
    logger = logging.getLogger(__name__)
    logger.info("Initializing configs")
    return Configs(MigrationDBConfig(), PathConfig())
