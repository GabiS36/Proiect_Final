import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser(unittest.TestCase):
    # instantiate chrome
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
# chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install()) nu mai merge - solution mai sus
    chrome.implicitly_wait(10)
    chrome.maximize_window()

    def close(self):
        self.chrome.delete_all_cookies()
        self.chrome.quit()
