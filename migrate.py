#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from src import configs, MigrationApplicationSelector


def main():
    cfg = configs.init_configs()
    selector = MigrationApplicationSelector(cfg)
    app = selector.select_by_argv(sys.argv[1:])
    return app.main() or 0


if __name__ == "__main__":
    sys.exit(main())
