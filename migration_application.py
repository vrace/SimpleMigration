#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import traceback

from tasks import collect_landing_tasks, collect_staging_tasks, collect_consumption_tasks, collect_misc_tasks

logger = logging.getLogger(__name__)


class MigrationApplication:

    def __init__(self, cfg):
        self.cfg = cfg

    def main(self):
        logger.info("Migration started")
        try:
            self.exec_landing_tasks()
            self.exec_staging_tasks()
            self.exec_consumption_tasks()
            self.exec_misc_tasks()
            logger.info("Migration completed")
            return 0
        except BaseException as exc:
            logger.error(f"Migration aborted: {exc}")
            logger.debug(f"{traceback.format_exc()}")
            return 1

    def exec_landing_tasks(self):
        tasks = collect_landing_tasks(self.cfg)
        self.exec_tasks_in_batch(tasks, "landing")

    def exec_staging_tasks(self):
        tasks = collect_staging_tasks(self.cfg)
        self.exec_tasks_in_batch(tasks, "staging")

    def exec_consumption_tasks(self):
        tasks = collect_consumption_tasks(self.cfg)
        self.exec_tasks_in_batch(tasks, "consumption")

    def exec_misc_tasks(self):
        tasks = collect_misc_tasks(self.cfg)
        self.exec_tasks_in_batch(tasks, "misc")

    def exec_tasks_in_batch(self, tasks, tasks_desc):
        if not tasks:
            logger.warning(f"No {tasks_desc} tasks")
            return
        logger.info(f"Executing {tasks_desc} tasks")
        has_error = False
        for task in tasks:
            try:
                task.execute()
            except BaseException as exc:
                logger.error(f"Problem executing {tasks_desc} task: {exc}")
                logger.debug(f"{traceback.format_exc()}")
                has_error = True
        if has_error:
            raise RuntimeError(f"Execute {tasks_desc} tasks are not fully completed")
