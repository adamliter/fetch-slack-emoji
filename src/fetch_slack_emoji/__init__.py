# -*- mode: python; coding: utf-8; fill-column: 88; -*-
from typing import Any

LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": """
            %(asctime)s
            %(levelname)s
            %(message)s
            %(module)s
            %(name)s
            """,
            "rename_fields": {
                "asctime": "@timestamp",
                "levelname": "level",
                "message": "msg",
            },
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "json": {
            "formatter": "json",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "__main__": {
            "level": "DEBUG",
            "handlers": ["json"],
            "propagate": False,
        },
        "fetch_slack_emoji": {
            "level": "DEBUG",
            "handlers": ["json"],
            "propagate": False,
        },
    },
    "root": {
        "level": "WARNING",
        "handlers": ["json"],
    },
}
