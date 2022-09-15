#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .configs import Configs
from .logging_config import *
from .migration_db_config import MigrationDBConfig
from .path_config import PathConfig

logger = logging.getLogger(__name__)


def init_configs():
    logger.info("Initializing configs")
    return Configs(MigrationDBConfig(), PathConfig())
