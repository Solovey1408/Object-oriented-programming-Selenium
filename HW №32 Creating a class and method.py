from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test:

    base_url = 'https://www.saucedemo.com/'
    window_width = 1920
    window_height = 1080


    def __init__(self):

        self._init_driver()


    def _init_driver(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_window_size(self.window_width, self.window_height)


    def test_select_product(self):

        self.driver.get(self.base_url)


start_test = Test()
start_test.test_select_product()