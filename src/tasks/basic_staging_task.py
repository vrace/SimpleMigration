#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


class BasicStagingTask:

    def __init__(self, cfg, staging_name, source=None, writer=None):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.staging_name = staging_name
