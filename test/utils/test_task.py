#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TestTask:

    def __init__(self, cfg, name, raise_exec_err=False):
        self.cfg = cfg
        self.name = name
        self.executed = False
        self.raise_exec_err = raise_exec_err

    def execute(self):
        self.executed = True
        if self.raise_exec_err:
            raise RuntimeError("raise execute error")
