from selenium import webdriver
from time import sleep
import unittest

# 创建一个类，名为test_baidu，继承unittest下的TestCase
class test_baidu(unittest.TestCase):
	
	# 初始化方法 每次执行用例的时候先执行此方法
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.url = "http://www.baidu.com"
		self.driver.get(self.url)
	
	# 结束方法 每次用例执行完毕后执行此方法
	def tearDown(self):
		self.driver.quit()

	# 测试用例，以“test”开头的为一条用例
	# 定义一条测试用例，名为test_search01
	def test_search01(self):
		dr = self.driver
		dr.find_element_by_id("kw").send_keys('selenium')
		dr.find_element_by_id('su').click()
		sleep(2)
		title = dr.title # 获取当前网页的标题，赋值给变量title
		self.assertEqual(title,"selenium_百度搜索") # 设置断言，利用assertEqual()判断当前标题是否与title相同

	# 定义一条测试用例，名为test_search02
	def test_search02(self):
		dr = self.driver
		dr.find_element_by_id("kw").send_keys('unittest')
		dr.find_element_by_id('su').click()
		sleep(2)
		url = dr.current_url # 获取当前网页的url地址，赋值给变量url
		self.assertIn("unittest",url) # 设置断言，利用assertIn()判断当前url地址是否包含"unittest"的值

if __name__ == '__main__':
	unittest.main()
		
