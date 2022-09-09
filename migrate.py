#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import configs
from migration_application import MigrationApplication

if __name__ == "__main__":
    cfg = configs.init_configs()
    app = MigrationApplication(cfg)
    sys.exit(app.main() or 0)
