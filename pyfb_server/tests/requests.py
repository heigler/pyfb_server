#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import unittest
from pyfb_server import settings

listen = 'http://127.0.0.1:%i' % settings.SERVER_PORT


class TestUserAppAuth(unittest.TestCase):
    pass

    
class TestUserBaseData(unittest.TestCase):
    
    def setUp(self):
        self.url = '%s/%s' % (listen, settings.GH_USER_URL.replace('(userid)', '100000000000001'))
        
    
    def test_response_type(self):
        req = urllib2.Request(self.url)
        response = urllib2.urlopen(req).read()
    
        self.assertTrue(json.loads(response))
        
    
    def test_response_content(self):
        req = urllib2.Request(self.url)
        response = urllib2.urlopen(req).read()
        
        self.assertTrue('id' in response)
        self.assertTrue('name' in response)
        self.assertTrue('first_name' in response)
        self.assertTrue('last_name' in response)
        self.assertTrue('link' in response)
        self.assertTrue('gender' in response)
        self.assertTrue('locale' in response)


        
if __name__ == '__main__':
    unittest.main()