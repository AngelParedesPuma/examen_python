import sys
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.by import By


class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()


    def test_reto_final_caso_textbox(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        name = driver.find_element_by_xpath("//input[@id='userName']")
        email = driver.find_element_by_xpath("//input[@id='userEmail']")
        address = driver.find_element_by_xpath("//textarea[@id='currentAddress']")
        permanent = driver.find_element_by_xpath("//textarea[@id='permanentAddress']")
        submit = driver.find_element_by_xpath("//button[@id='submit']")
        name.send_keys("ANGEL")
        time.sleep(1)
        email.send_keys("CORREO@CORREO.com")
        time.sleep(1)
        address.send_keys("lima 123 lima-Peru")
        time.sleep(1)
        permanent.send_keys("Lima")
        time.sleep(5)
        submit.click()
        time.sleep(5)

        # codigo here!

    def test_reto_final_caso_radio_button(self):
        driver = self.driver
        driver.get("https://demoqa.com/radio-button")
        radio_button_impressive = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]")
        radio_button_impressive.click()
        text_output = driver.find_element_by_xpath("//span[contains(text(),'Impressive')] ")
        self.assertRegex(text_output.text, "Impressive")
        time.sleep(5)

    def test_reto_final_caso_webtables(self):
        driver = self.driver
        driver.get("https://demoqa.com/webtables")
        time.sleep(2)
        ver_registro = driver.find_element_by_xpath("//option[contains(text(),'5 rows')]")
        ver_registro.click()
        for x in ["Renzo","Pedro", "Angel","Yefri","rrr","eee","ww","rererer"]:
            nuevo = driver.find_element_by_xpath("//button[@id='addNewRecordButton']")
            nuevo.click()
            first_name = driver.find_element_by_xpath("//input[@id='firstName']")
            last_name = driver.find_element_by_xpath("//input[@id='lastName']")
            email = driver.find_element_by_xpath("//input[@id='userEmail']")
            age = driver.find_element_by_xpath("//input[@id='age']")
            salary = driver.find_element_by_xpath("//input[@id='salary']")
            departament = driver.find_element_by_xpath("//input[@id='department']")
            submit = driver.find_element_by_xpath("//button[@id='submit']")
            first_name.send_keys(x)
            last_name.send_keys("canvia")
            email.send_keys("correo@correo.com")
            age.send_keys("39")
            salary.send_keys("1000")
            departament.send_keys("lima")
            submit.click()

        next = driver.find_element_by_xpath("//button[contains(text(),'Next')]")
        previuos = driver.find_element_by_xpath("//button[contains(text(),'Previous')]")
        next.click()
        previuos.click()
        buscar = driver.find_element_by_xpath("// input[ @ id = 'searchBox']")
        buscar.send_keys("Renzo")
        lupa = driver.find_element_by_xpath("//span[@id='basic-addon2']")
        lupa.click()
        time.sleep(3)
        pos = driver.find_element_by_css_selector("span[title='Edit']")
        pos.click()
        time.sleep(9)
        first_name = driver.find_element_by_xpath("//input[@id='firstName']")
        first_name.clear()
        first_name.send_keys("Renato")
        time.sleep(7)
        confirma = driver.find_element_by_xpath("// button[ @ id = 'submit']")
        confirma.click()
        buscar.click()
        buscar.clear()
        buscar.send_keys("Renato")
        time.sleep(10)
        # codigo here!

    def test_reto_final_caso_buttons(self):
        driver = self.driver
        driver.get("https://demoqa.com/buttons")
        action = ActionChains(self.driver)
        time.sleep(4)
        button1 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]")
        button2 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/button[1]")
        button3 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]")
        action.double_click(button1)
        time.sleep(2)
        action.context_click(button2).perform()
        time.sleep(2)
        button3.click()
        time.sleep(5)

        # codigo here!


if __name__ == '__main__':
    unittest.main()
