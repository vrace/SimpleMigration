#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .migration_application import MigrationApplication


class MigrationApplicationSelector:

    def __init__(self, cfg):
        self.cfg = cfg

    def select_by_argv(self, argv):
        if not argv:
            return MigrationApplication(self.cfg)

        name = argv[0]
        args = argv[1:]

        raise ValueError(f"unable to select application '{name}'")
