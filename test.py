from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os


def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)

browser = webdriver.Chrome(executable_path=resource_path('./chromedriver'))
browser.get('https://yahoo.co.jp')