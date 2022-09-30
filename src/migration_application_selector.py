#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .migration_application import MigrationApplication
from .migration_execute_task_application import MigrationExecuteTaskApplication


class MigrationApplicationSelector:

    def __init__(self, cfg):
        self.cfg = cfg

    def select_by_argv(self, argv):
        if not argv:
            return MigrationApplication(self.cfg)

        name = argv[0]
        args = argv[1:]

        if name == "migrate":
            return MigrationApplication(self.cfg)
        if name == "land":
            return MigrationExecuteTaskApplication(self.cfg, "landing", args)
        if name == "stage":
            return MigrationExecuteTaskApplication(self.cfg, "staging", args)
        if name == "consume":
            return MigrationExecuteTaskApplication(self.cfg, "consumption", args)
        if name == "misc":
            return MigrationExecuteTaskApplication(self.cfg, "misc", args)

        raise ValueError(f"unable to select application '{name}'")
