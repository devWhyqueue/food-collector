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
        thread_element = self._web.driver.find_elements_by_css_selector('.forum_threads .thread')
        threads = []
        for thread in thread_element:
            threads.append((thread.find_element_by_class_name('thread-title').text,
                            thread.find_element_by_class_name('time').text))
        threads = list(filter(lambda t: not re.match('vor .* (Stunde|Tag|Monat|Jahr)', t[1]), threads[3:]))
        if not threads:
            log.info('No new posts found.')
        self._web.driver.quit()
        return threads

    def _login(self):
        self._web.driver.find_element_by_id('login-email').click()
        self._web.driver.find_element_by_id('login-email').send_keys(self._user.username)
        self._web.driver.find_element_by_id('login-password').send_keys(self._user.password)
        self._web.driver.find_element_by_id('login-btn').click()
