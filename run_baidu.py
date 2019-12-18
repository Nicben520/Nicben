from baidu import 百度,unittest

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(test_baidu("test_search01"))
	suite.addTest(test_baidu("test_search02"))
	runner = unittest.TextTestRunner(verbosity=1)
	runner.run(suite)