#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


class ConfigParser:
    @staticmethod
    def parse(value):
        if not value:
            return value
        if value.startswith("\\"):
            return value[1:]
        if not value.startswith("$"):
            return value
        if ':' in value:
            env_name, default_value = value.split(':', 1)
            env_name = env_name[1:]
        else:
            env_name = value[1:]
            default_value = None
        return os.getenv(env_name, default=default_value)
