from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Общий класс
class Test():


    #Метод
    def test_select_product(self):

        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.set_window_size(1920, 1080)


start_test = Test() #Экземпляр класса
start_test.test_select_product() #Вызов метода