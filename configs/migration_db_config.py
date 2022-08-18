#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine


class MigrationDBConfig:

    url = "postgresql://postgres:postgres@localhost:5432/postgres"

    @staticmethod
    def connect():
        return create_engine(MigrationDBConfig.url)
