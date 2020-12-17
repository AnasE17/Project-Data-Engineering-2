import unittest
import requests

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText


class TestClassifier(unittest.TestCase):
    
    def test_obama(self):
        rep=requests.post('http://localhost:5000/', data=params)
        params = {
           'txt': "Obama",
           "form_type": "submit_txt"
        }
        print("Testing Obama as a query \n")
        print("result :"+rep.content+"\n")
        self.assertEqual(response.status_code,200)

    def test_hillary(self):
        rep=requests.post('http://localhost:5000/', data=params)
        params = {
            'txt': "hillary",
            "form_type": "submit_txt"
        }
        print("Testing Hillary as a query \n")
        print("result :"+rep.content+"\n")
        self.assertEqual(response.status_code,200)

 


if __name__ == '__main__':
    unittest.main()
