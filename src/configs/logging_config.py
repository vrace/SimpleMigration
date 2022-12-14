#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def init_logging():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s --- %(name)s : %(message)s",
        level=logging.DEBUG
    )
