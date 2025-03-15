from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Test:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_window_size(1920, 1080)

    #Метод
    def test_select_product(self):

        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)


start_test = Test()
start_test.test_select_product()