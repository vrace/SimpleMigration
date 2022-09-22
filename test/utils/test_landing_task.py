#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestLandingTask:

    def __init__(self, cfg, table_name, raise_exec_err=False):
        self.cfg = cfg
        self.table_name = table_name
        self.executed = False
        self.raise_exec_err = raise_exec_err

    def execute(self):
        self.executed = True
        if self.raise_exec_err:
            raise RuntimeError("raise execute error")
