# -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
from settings import LOG_LEVEL, DEBUG


def getLogger(name):
    if DEBUG:
        handler = StreamHandler()
    else:
        filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs/www.log")
        if not os.path.exists(filename):
            os.system('touch %s' % filename)

        handler = TimedRotatingFileHandler(filename, when='d')

    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)
    logger.propagate = 0

    return logger
