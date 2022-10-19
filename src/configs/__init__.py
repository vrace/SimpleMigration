#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config_loader import ConfigLoader
from .configs import Configs
from .logging_config import init_logging
from .migration_db_config import MigrationDBConfig
from .path_config import PathConfig


def init_configs():
    init_logging()
    loader = ConfigLoader()
    return loader.load()
