from selenium import webdriver
from time import sleep
import unittest

class test_baidu(unittest.TestCase):
	# 初始化方法
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.baidu.com"
		self.driver.get(self.url)
	# 结束方法
	def tearDown(self):
		self.driver.quit()

	def test_search01(self):
		dr = self.driver
		dr.find_element_by_id("kw").send_keys('selenium')
		dr.find_element_by_id('su').click()
		sleep(2)
		title = dr.title
		self.assertEqual(title,"selenium_百度搜索")
	def test_search02(self):
		dr = self.driver
		dr.find_element_by_id("kw").send_keys('unittest')
		dr.find_element_by_id('su').click()
		sleep(2)
		url = dr.current_url
		self.assertIn("unittest",url)

if __name__ == '__main__':
	unittest.main()
		
