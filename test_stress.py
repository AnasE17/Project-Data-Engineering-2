import unittest
import time

try:
    from .model import get_tweet_similar, preprocessText, load_model
except ImportError:
    from model import get_tweet_similar, preprocessText, load_model


class TestClassifier(unittest.TestCase):

	
	def stress_test(self):
		start = time.time()
		for i in range(1000):
			params = {
				'txt': "test",
				"form_type": "submit_txt"
			}
			rep=requests.post('http://localhost:5000/', data=params)
		end = time.time()
		self.assertGreater(60 , end-start)


 


if __name__ == '__main__':
    unittest.main()
