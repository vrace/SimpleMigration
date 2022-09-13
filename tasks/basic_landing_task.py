#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

from tasks.writer import BasicSqlWriter


class BasicLandingTask:

    def __init__(self, cfg, source, writer=None):
        self.cfg = cfg
        self.source = source
        self.writer = writer or BasicSqlWriter(cfg.db)

    def execute(self):
        module_name = self.source.get_module_name()
        if_exists = "replace"
        with self.source.open(self.cfg) as chunks:
            for chunk in chunks:
                df = pd.DataFrame(chunk)
                self.writer.write(df, module_name, if_exists)
                if if_exists == "replace":
                    if_exists = "append"
