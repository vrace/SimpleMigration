#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine


class MigrationDBConfig:

    def __init__(self):
        self.url = "postgresql://postgres:postgres@localhost:5432/postgres"

    def connect(self):
        return create_engine(self.url)
