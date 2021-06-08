import logging.config
from pathlib import Path
from time import sleep

import click
import pkg_resources
from click import command, option

from foodcollector.foodsharing import IntroCollectionFinder
from foodcollector.messaging import SMSNotifier, build_message
from foodcollector.models import User
from foodcollector.webdriver import Web

logging_config = pkg_resources.resource_filename(__name__, str(Path('config/logging.ini')))
logging.config.fileConfig(logging_config, disable_existing_loggers=False)


@command()
@option('--username', required=True)
@option('--password', required=True)
@option('--phone-number', required=True)
@option('--chromium-path', type=click.Path())
def cli(username, password, chromium_path, phone_number):
    intro_collection = IntroCollectionFinder(Web(chromium_path), User(username, password))
    notifier = SMSNotifier(phone_number)
    while True:
        threads = intro_collection.find_updated_threads()
        if threads:
            msg = build_message(threads)
            notifier.send_message(msg)
        sleep(3600)


if __name__ == '__main__':
    cli()
