#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from .config_parser import ConfigParser


class MigrationDBConfig:

    def __init__(self):
        self.host = ConfigParser.parse("$DB_HOST:localhost")
        self.port = ConfigParser.parse("$DB_PORT:5432")
        self.user = ConfigParser.parse("$DB_USER:postgres")
        self.password = ConfigParser.parse("$DB_PASSWORD:postgres")
        self.database = ConfigParser.parse("$DB_DATABASE:postgres")

    def create_url(self):
        return URL.create(
            drivername="postgresql",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )

    def connect(self):
        return create_engine(self.create_url())
