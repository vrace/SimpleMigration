#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BasicTask:

    def __init__(self, name):
        self.name = name

    def create_reader(self):
        raise NotImplementedError()

    def create_writer(self):
        raise NotImplementedError()

    def execute_begin(self):
        pass

    def execute_end(self, num_rows):
        pass

    def execute_transform_chunk(self, df):
        pass

    def execute(self):
        self.execute_begin()
        if_exists = "replace"
        num_rows = 0
        reader = self.create_reader()
        writer = self.create_writer()
        with reader.read() as chunks:
            for df in chunks:
                self.execute_transform_chunk(df)
                writer.write(df, if_exists)
                num_rows += len(df)
                if if_exists == "replace":
                    if_exists = "append"
        self.execute_end(num_rows)
