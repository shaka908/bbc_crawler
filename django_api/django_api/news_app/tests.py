from django.test import TestCase
from django.test import Client
import json

# Create your tests here.
class SearchOrViewSetTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def tearDown(self):
        pass

    def test_list_endpoint_should_return_200(self):
        resp = self.c.get('/search_or/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_return_200(self):
        resp = self.c.get('/search_or/catholic church/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_return_correct_content(self):
        resp = self.c.get('/search_or/catholic church/')
        result = resp.content
        flag = True
        for x in json.loads(result):
            # title = x.get('title')
            # content = x.get('contnet')
            s = json.dumps(x)
            if ('catholic' not in s.lower()) and ('church' not in s.lower()):
                flag = False
        self.assertTrue(flag == True)

class SearchAndViewSetTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def tearDown(self):
        pass

    def test_list_endpoint_should_return_200(self):
        resp = self.c.get('/search_and/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_return_200(self):
        resp = self.c.get('/search_and/catholic church/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_return_correct_content(self):
        resp = self.c.get('/search_and/catholic church/')
        result = resp.content
        flag = True
        for x in json.loads(result):
            # title = x.get('title')
            # content = x.get('contnet')
            s = json.dumps(x)
            if 'catholic church' not in s.lower():
                # print s
                flag = False
        self.assertTrue(flag == True)

class LookupUrlViewSetTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def tearDown(self):
        pass

    def test_list_endpoint_should_return_200(self):
        resp = self.c.get('/lookup_url/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_return_correct_content(self):
        resp = self.c.get('/lookup_url/education-36144084/')
        flag = False
        if 'education' in resp.content:
            flag = True
        self.assertTrue(flag == True, resp.status_code == 200)


class LookupDateViewSetTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def tearDown(self):
        pass

    def test_list_endpoint_should_return_200(self):
        resp = self.c.get('/lookup_date/')
        self.assertTrue(resp.status_code == 200)

    def test_details_endpoint_should_raise_error_with_incorrect_date(self):
        resp = self.c.get('/lookup_date/abc/')
        self.assertTrue(resp.status_code == 400)


    def test_details_endpoint_should_return_correct_content(self):
        resp = self.c.get('/lookup_date/27 April 2016/')
        flag = True
        result = resp.content
        # print result
        for x in json.loads(result):
            if x['datetime'] != '27 April 2016':
                flag = False
        self.assertTrue(flag == True, resp.status_code == 200)
