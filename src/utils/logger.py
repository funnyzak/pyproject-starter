#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import os
import time


LOG_PATH = os.path.join(os.getcwd(), "_logs")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


def new_logger(log_name=None):
    if log_name is None:
        # 获取入口文件名（不包含扩展名）
        log_name = "logger_{}.log".format(time.strftime("%Y%m%d%H%M%S"))
    logger = logging.getLogger(os.path.splitext(log_name)[0])
    LOG_FILENAME = os.path.join(LOG_PATH, log_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(process)d-%(threadName)s - " "%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


logger = new_logger()
