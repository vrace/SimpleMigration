#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .basic_landing_task import BasicLandingTask
from .source import CsvSource


def collect_landing_tasks(cfg):
    return [
        BasicLandingTask(cfg, CsvSource("person.csv")),
        BasicLandingTask(cfg, CsvSource("pet.csv")),
    ]


def collect_staging_tasks(cfg):
    return []


def collect_consumption_tasks(cfg):
    return []


def collect_misc_tasks(cfg):
    return []
