#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from src import configs, MigrationApplication


def main():
    cfg = configs.init_configs()
    app = MigrationApplication(cfg)
    return app.main() or 0


if __name__ == "__main__":
    sys.exit(main())
