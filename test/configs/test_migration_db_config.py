#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from src.configs import MigrationDBConfig


class TestMigrationDBConfig(TestCase):

    def test_create_url(self):
        cfg = MigrationDBConfig()
        cfg.host = "host"
        cfg.port = "port"
        cfg.user = "user"
        cfg.password = "password"
        cfg.database = "database"
        expect = "postgresql://user:password@host:port/database"
        self.assertEqual(cfg.create_url(), expect)
