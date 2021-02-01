from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
PATH = "C:\Program Files (x86)\chromedriver.exe"

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        
    def test_shopping_cart(self):
        driver = self.driver
        driver.get("https://www.jimms.fi/")
        self.assertIn("Jimm's", driver.title)
        
        category = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Komponentit"))
        )
        category.click()
        subcategory = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Näytönohjaimet"))
        )
        subcategory.click()
        Sorting  = driver.find_element_by_class_name("sortitems")
        options = Sorting.find_elements_by_tag_name("option")
        for option in options:
            if option.text == "Hinta (Suurin-Pienin)":
                option.click()
        cart = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.LINK_TEXT, "LISÄÄ KORIIN"))
        )
        cart.click()
        find_cart = driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[6]/a")
        find_cart.click()
        find_cart_link = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[6]/div/div/div[1]/div/a/span"))
         )
        find_cart_link.click()
        assert "tyhjä" not in driver.page_source
        print("ITEM ADDED AND FOUND TO BASKET")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()