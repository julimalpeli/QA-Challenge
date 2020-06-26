import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import time

PATH = "C:\\AutomationSuit-ContactForm-Exercise2\\chromedriver.exe"

class suit(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(PATH)

	def test_SubjectHeading_Field_TC2Step4(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=contact")
		time.sleep(1)
		select = driver.find_element_by_xpath("//*[@id='id_contact']")
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='id_contact']"))
		seleccionar.select_by_value("0")
		time.sleep(1)
		validate_email = driver.find_element_by_xpath("//*[@id='email']")
		validate_email.send_keys("julianmalpeli@gmail.com")
		time.sleep(1)
		validate_order_reference = driver.find_element_by_xpath("//*[@id='id_order']")
		validate_order_reference.send_keys("N222")
		time.sleep(1)
		driver.find_element_by_id("fileUpload").send_keys("C:\\AutomationSuit-ContactForm-Exercise2\\TestFile.txt")
		time.sleep(1)
		validate_message = driver.find_element_by_xpath("//*[@id='message']")
		validate_message.send_keys("My message is the following")
		time.sleep(1)
		send_message = driver.find_element_by_id("submitMessage").click()
		time.sleep(2)
		#error=driver.find_element_by_tag_name("body").text
		error=driver.find_element_by_xpath("//*[@id='center_column']").text
		print(error)
		self.assertIn("There is 1 error",error)


	def test_Email_Field_TC2Step6(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=contact")
		time.sleep(1)
		select = driver.find_element_by_xpath("//*[@id='id_contact']")
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='id_contact']"))
		seleccionar.select_by_value("2")
		time.sleep(1)
		validate_email = driver.find_element_by_xpath("//*[@id='email']")
		validate_email.send_keys("julianmalpeligmail.com")
		time.sleep(1)
		validate_order_reference = driver.find_element_by_xpath("//*[@id='id_order']")
		validate_order_reference.send_keys("N222")
		time.sleep(1)
		driver.find_element_by_id("fileUpload").send_keys("C:\\AutomationSuit-ContactForm-Exercise2\\TestFile.txt")
		time.sleep(1)
		validate_message = driver.find_element_by_xpath("//*[@id='message']")
		validate_message.send_keys("My message is the following")
		time.sleep(1)
		send_message = driver.find_element_by_id("submitMessage").click()
		time.sleep(2)
		#error=driver.find_element_by_tag_name("body").text
		error=driver.find_element_by_xpath("//*[@id='center_column']").text
		print(error)
		self.assertIn("There is 1 error",error)

	def test_OrderReference_Field_TC2Step7(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=contact")
		time.sleep(1)
		select = driver.find_element_by_xpath("//*[@id='id_contact']")
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='id_contact']"))
		seleccionar.select_by_value("2")
		time.sleep(1)
		validate_email = driver.find_element_by_xpath("//*[@id='email']")
		validate_email.send_keys("julianmalpeli@gmail.com")
		time.sleep(1)
		driver.find_element_by_id("fileUpload").send_keys("C:\\AutomationSuit-ContactForm-Exercise2\\TestFile.txt")
		time.sleep(1)
		validate_message = driver.find_element_by_xpath("//*[@id='message']")
		validate_message.send_keys("My message is the following")
		time.sleep(1)
		send_message = driver.find_element_by_id("submitMessage").click()
		time.sleep(2)
		#error=driver.find_element_by_tag_name("body").text
		error=driver.find_element_by_xpath("//*[@id='center_column']").text
		print(error)
		self.assertIn("There is 1 error",error)
		

	def test_AttachFile_Field_TC2Step8(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=contact")
		time.sleep(1)
		select = driver.find_element_by_xpath("//*[@id='id_contact']")
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='id_contact']"))
		seleccionar.select_by_value("2")
		time.sleep(1)
		validate_email = driver.find_element_by_xpath("//*[@id='email']")
		validate_email.send_keys("julianmalpeli@gmail.com")
		time.sleep(1)
		validate_order_reference = driver.find_element_by_xpath("//*[@id='id_order']")
		validate_order_reference.send_keys("N222")
		time.sleep(1)
		validate_message = driver.find_element_by_xpath("//*[@id='message']")
		validate_message.send_keys("My message is the following")
		time.sleep(1)
		send_message = driver.find_element_by_id("submitMessage").click()
		time.sleep(2)
		#error=driver.find_element_by_tag_name("body").text
		error=driver.find_element_by_xpath("//*[@id='center_column']").text
		print(error)
		self.assertIn("There is 1 error",error)
		


	def test_Message_Field_TC2Step9(self):
		driver = self.driver
		driver.get("http://automationpractice.com/index.php?controller=contact")
		time.sleep(1)
		select = driver.find_element_by_xpath("//*[@id='id_contact']")
		seleccionar = Select(driver.find_element_by_xpath("//*[@id='id_contact']"))
		seleccionar.select_by_value("2")
		time.sleep(1)
		validate_email = driver.find_element_by_xpath("//*[@id='email']")
		validate_email.send_keys("julianmalpeli@gmail.com")
		time.sleep(1)
		validate_order_reference = driver.find_element_by_xpath("//*[@id='id_order']")
		validate_order_reference.send_keys("N222")
		time.sleep(1)
		driver.find_element_by_id("fileUpload").send_keys("C:\\AutomationSuit-ContactForm-Exercise2\\TestFile.txt")
		time.sleep(1)
		send_message = driver.find_element_by_id("submitMessage").click()
		time.sleep(2)
		#error=driver.find_element_by_tag_name("body").text
		error=driver.find_element_by_xpath("//*[@id='center_column']").text
		print(error)
		self.assertIn("There is 1 error",error)


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'Result of Automation Test Suit'))
