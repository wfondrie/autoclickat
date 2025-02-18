# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "pyautogui",
# ]
# ///
import time
import logging
from datetime import datetime, date

import click
import pyautogui

LOGGER = logging.getLogger(__name__)


@click.command()
@click.argument("target", type=click.DateTime(formats=["%H:%M:%S"]))
def main(target: click.DateTime) -> None:
    """Click at the specified time.

    TIME is a string representing a date and time in the format
    'HH:MM:SS' in the local timezone.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    local_time = datetime.fromtimestamp(time.time())
    target_time = datetime.combine(date.today(), target.time())
    diff = target_time - local_time

    LOGGER.info("Current time: %s", local_time.time())
    LOGGER.info("Target time:  %s", target_time.time())
    LOGGER.info("Waiting:      %ss", diff.total_seconds())

    time.sleep(diff.total_seconds())
    pyautogui.click()



if __name__ == "__main__":
    main()
