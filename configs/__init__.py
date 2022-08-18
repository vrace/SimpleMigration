#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .logging_config import *
from .path_config import PathConfig

logger = logging.getLogger(__name__)


def init_configs():
    logger.info("Initializing configs")
