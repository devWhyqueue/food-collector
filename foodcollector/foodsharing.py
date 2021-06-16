import logging
import re

from foodcollector.models import User
from foodcollector.webdriver import Web

log = logging.getLogger(__name__)


class IntroCollectionFinder:
    BASE_URL = 'https://foodsharing.de/?page=login&ref=%2F%3Fpage%3Dbezirk%26bid%3D2710%26sub%3Dforum'

    def __init__(self, web: Web, user: User):
        self._web = web
        self._user = user

    def find_updated_threads(self):
        log.info('Looking for new posts...')
        self._web.driver.get(IntroCollectionFinder.BASE_URL)
        self._login()
        threads = self._web.driver.find_elements_by_css_selector('.forum_threads .thread')
        updated_threads = []
        for thread in threads:
            if re.match('vor .* Minuten', thread.find_element_by_class_name('time').text):
                updated_threads.append(thread.find_element_by_class_name('thread-title').text)
                log.info(f'New post in {updated_threads[-1]}!')
        if not updated_threads:
            log.info('No new posts found.')
        return updated_threads

    def _login(self):
        self._web.driver.find_element_by_id('login-email').send_keys(self._user.username)
        self._web.driver.find_element_by_id('login-password').send_keys(self._user.password)
        self._web.driver.find_element_by_id('login-btn').click()
