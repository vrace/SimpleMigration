#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import traceback

from src.tasks import collect_landing_tasks


class MigrationExecuteLandingApplication:

    def __init__(self, cfg, names):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.names = names

    def main(self):
        self.logger.info("Migration execute landing started")
        tasks = self.collect_tasks()
        num_errors = self.execute_tasks(tasks)
        if num_errors:
            self.logger.error("Migration not fully completed")
            self.logger.error(f"...{num_errors} of {len(tasks)} tasks failed")
            return 1
        self.logger.info("Migration completed")
        return 0

    def collect_tasks(self):
        tasks = [x for x in collect_landing_tasks(self.cfg) if x.table_name in self.names]
        found = [x.table_name for x in tasks]
        missing = [x for x in self.names if x not in found]
        if missing:
            self.logger.warning("Not all landing tasks are collected")
            for x in missing:
                self.logger.warning(f"...{x}")
        return tasks

    def execute_tasks(self, tasks):
        if not tasks:
            self.logger.warning("There is no task to execute")
            return 0
        num_errors = 0
        for task in tasks:
            try:
                task.execute()
            except BaseException as exc:
                self.logger.error(f"Problem executing landing '{task.table_name}': {exc}")
                self.logger.debug(f"{traceback.format_exc()}")
                num_errors += 1
        return num_errors
