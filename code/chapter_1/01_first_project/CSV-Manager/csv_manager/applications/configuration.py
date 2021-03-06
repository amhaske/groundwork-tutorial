#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

APP_NAME = "csv_manager_app"
APP_DESCRIPTION = "groundwork application of package CSV-Manager"
APP_PATH = os.path.join(os.path.expanduser('~'), "CSV-Manager")

PLUGINS = ["csv_manager_plugin", "GwPluginsInfo"]

GROUNDWORK_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s - %(levelname)-5s - %(message)s"
        },
        'debug': {
            'format': "%(asctime)s - %(levelname)-5s - %(name)-40s - %(message)-80s - %(module)s:%("
                      "funcName)s(%(lineno)s)"
        },
    },
    'handlers': {
        'console_stdout': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'level': 'INFO'
        },
        'file': {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "debug",
            "filename": os.path.join(APP_PATH, "csv_manager.log"),
            "maxBytes": 1024000,
            "backupCount": 3,
            'level': 'DEBUG'
        },
        # 'file_my_plugin': {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "formatter": "debug",
        #     "filename": "logs/my_plugin.log",
        #     "maxBytes": 1024000,
        #     "backupCount": 3,
        #     'level': 'DEBUG'
        # },
    },
    'loggers': {
        '': {
            'handlers': ['console_stdout'],
            'level': 'DEBUG',
            'propagate': False
        },
        'groundwork': {
            'handlers': ['console_stdout', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        # 'MyPlugin': {
        #     'handlers': ['console_stdout', 'file_my_plugin'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
    }
}
