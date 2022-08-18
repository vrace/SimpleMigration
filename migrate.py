#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from migration_application import MigrationApplication

if __name__ == "__main__":
    app = MigrationApplication()
    sys.exit(app.main() or 0)
