from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Web:
    def __init__(self, chromium_path=None):
        options = Options()
        options.headless = True
        options.add_argument('window-size=1920x1080')
        if chromium_path:
            options.binary_location = chromium_path
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
