#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from sqlalchemy.engine import URL

from src.configs import MigrationDBConfig


class TestMigrationDBConfig(TestCase):

    def test_create_url(self):
        cfg = MigrationDBConfig()
        cfg.host = "host"
        cfg.port = "5678"
        cfg.user = "user"
        cfg.password = "password"
        cfg.database = "database"
        expect = URL.create(
            drivername="postgresql",
            username="user",
            password="password",
            host="host",
            port=5678,
            database="database"
        )
        self.assertEqual(cfg.create_url(), expect)
