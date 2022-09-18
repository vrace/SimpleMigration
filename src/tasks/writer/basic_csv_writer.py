#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .basic_writer import BasicWriter


class BasicCsvWriter(BasicWriter):

    def __init__(self, cfg, csv_name):
        self.cfg = cfg
        self.csv_name = csv_name

    def write(self, df, if_exists):
        mode, header = self.extract_write_args(if_exists)
        csv_file = self.cfg.path.data_out_file(f"{self.csv_name}.csv")
        df.to_csv(csv_file, mode=mode, header=header, index=False, float_format="%g")

    def extract_write_args(self, if_exists):
        if if_exists == "replace":
            return "w", True
        elif if_exists == "append":
            return "a", False
        raise ValueError("if_exists can only be 'replace' or 'append'")
