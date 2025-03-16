from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.set_window_size(*self.WINDOWS_SIZE)

    def test_select_product(self):
        self.driver.get(self.BASE_URL)

        print('Start Test')

        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys("standard_user")
        print('Input User name')

        user_password = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        user_password.send_keys("secret_sauce")
        print('Input password')

        button_login = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print('Click login button')

        select_product = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('Select Product')

        enter_shopping_cart = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='shopping_cart_link']")))
        enter_shopping_cart.click()
        print('Enter Cart')

        success_test = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='title']")))
        value_success_test = success_test.text

        assert value_success_test == 'Your Cart','Test Failed'
        print('Test Success')

start_test = Test()
start_test.test_select_product()