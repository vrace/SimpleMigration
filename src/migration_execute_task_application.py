#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import traceback

from .tasks import collect_landing_tasks, collect_staging_tasks, collect_consumption_tasks, collect_misc_tasks


class MigrationExecuteTaskApplication:

    def __init__(self, cfg, task_type, task_names):
        self.logger = logging.getLogger(__name__)
        self.cfg = cfg
        self.task_type = task_type
        self.task_names = task_names

    def main(self):
        self.logger.info(f"Migration execute {self.task_type} started")
        tasks = self.collect_tasks()
        num_errors = self.execute_tasks(tasks)
        if num_errors:
            self.logger.error("Migration not fully completed")
            self.logger.error(f"...{num_errors} of {len(tasks)} tasks failed")
            return 1
        self.logger.info("Migration completed")
        return 0

    def collect_tasks(self):
        collectors = {
            "landing": collect_landing_tasks,
            "staging": collect_staging_tasks,
            "consumption": collect_consumption_tasks,
            "misc": collect_misc_tasks,
        }
        collect_fn = collectors[self.task_type]
        if not self.task_names:
            return collect_fn(self.cfg)
        tasks = [x for x in collect_fn(self.cfg) if x.name in self.task_names]
        found = [x.name for x in tasks]
        missing = [x for x in self.task_names if x not in found]
        if missing:
            self.logger.warning("Not all tasks are collected")
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
                self.logger.error(f"Problem executing {self.task_type} '{task.name}': {exc}")
                self.logger.debug(f"{traceback.format_exc()}")
                num_errors += 1
        return num_errors
