from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test:
    BASE_URL = 'https://www.saucedemo.com/'
    WINDOWS_SIZE = (1920, 1080)


    def __init__(self):
        self._init_driver()


    def _init_driver(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_window_size(self.WINDOWS_SIZE)


    def test_select_product(self):
        self.driver.get(self.BASE_URL)


start_test = Test()
start_test.test_select_product()