# -*- mode: python; coding: utf-8; fill-column: 88; -*-
import json
import logging
import re
import shutil
from os.path import splitext
from pathlib import Path
from time import time
from typing import Annotated, Any

import typer
import urllib3

_logger: logging.Logger = logging.getLogger(__name__)


def _main(
    emoji_file: Annotated[
        Path, typer.Option(exists=True, file_okay=True, dir_okay=False, readable=True)
    ],
    out_dir: Annotated[
        Path, typer.Option(exists=False, file_okay=False, dir_okay=True, writable=True)
    ],
) -> None:
    _logger.info("Reading list of emoji from %(p)s", {"p": str(emoji_file)})

    with emoji_file.open("r") as f:
        emoji_payload: dict[str, Any] = json.load(f)
        emoji_list: list[tuple[str, str]] = [
            (k, v) for k, v in emoji_payload["emoji"].items()
        ]

    _logger.info("%(n)d emoji to download", {"n": len(emoji_list)})

    _logger.info("Target directory is %(d)s", {"d": str(out_dir)})
    if not out_dir.exists():
        _logger.debug("Target directory doesn't exist; creating it")
        out_dir.mkdir()

    _logger.info("Starting to download emoji")
    st: float = time()

    http: urllib3.PoolManager = urllib3.PoolManager(
        retries=urllib3.Retry(5, redirect=2, backoff_factor=0.1)
    )

    for name, url in emoji_list:
        if re.search("^alias:.*$", url) is not None:
            _logger.debug("%(u)s is an alias; skipping", {"u": url})
            continue

        _logger.debug("Downloading emoji called %(e)s", {"e": name})
        name: str = name + splitext(url)[1]
        out_file: Path = out_dir / name
        with (
            http.request("GET", url, preload_content=False) as resp,
            out_file.open("wb") as f,
        ):
            shutil.copyfileobj(resp, f)

    et: float = time()
    _logger.info("Finished downloading emoji after %(s).2f seconds", {"s": (et - st)})


def main() -> None:
    import logging.config

    from . import LOGGING_CONFIG

    logging.config.dictConfig(LOGGING_CONFIG)
    logging.captureWarnings(True)

    _ = typer.run(_main)
