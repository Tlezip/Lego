from django.test import TestCase,Client
from rest_framework.test import APIRequestFactory
from legotest.models import Test
from rest_framework.test import APITestCase,APIClient
from django.contrib.auth.models import User
from django.http import HttpRequest
import requests
import urllib
import json
from django.core import serializers
from legotest.serializer import TestSerializer
# Create your tests here.

class TestCase_Create(TestCase):
	
    def setUp(self):
        self.client = APIClient()

    # def test_by_default(self):
    # # """
    # # By default, the test client is CSRF exempt.
    # # """
    #     response = self.client.post('/lego/legotest/', {'name': 'Math Test', 
    #                                 'typetest' : "Choice", 
    #                                 'category' : "AIS Products", 
    #                                 'overview' : "This is overview", 
    #                                 'provider' : "Tlezip",
    #                                 'conndition' : "This is condition detail",
    #                                 'max_submit' : 5, 
    #                                 'limit' : 0, 
    #                                 'expired' : 0,
    #                                 'descripe' : "This is descripe",}, format='json')
    #     print(response.content)
    #     assert response.status_code != 200

    def test_get(self):
        response = self.client.get('/api/test/')
        assert response.status_code == 200

    def test_post(self):
        response = self.client.post('/api/test/', {'name': 'Math Test'}, format='json')
        assert response.status_code == 403

    def test_put(self):
        response = self.client.put('/api/test/', {'name': 'Math Test'}, format='json')
        assert response.status_code == 403

    def test_patch(self):
        response = self.client.patch('/api/test/', {'name': 'Math Test'}, format='json')
        assert response.status_code == 403

    def test_idp(self):
        response = urllib.request.urlopen('http://localhost:8000/api/test/')
        data = json.load(response)
        output_dict = [x for x in data if x['name'] == 'Tlezip']
        print(output_dict)
        print("\n")
        b = Test.objects.create(name="Tlezip", is_display = True, id=3, category=2, overview="zzz", condition="xc", descripe='')
        c = TestSerializer(b)
        print(c.data)
        assert c.data not in data
        
        # b = list(Test.objects.filter(name="Tlezip"))
        # assert b_as_json == data
        # a = Test.objects.create(name="Tlezip", is_display = False,)
        # a = list(Test.objects.filter(name="Tlezip"))
        # assert a not in getdata
        # print(c.context['name'])
        # response = c.get('/api/test/')
        # c = Client()
        # response = self.client.get('/api/test/')
        # print(response.json())

        # if a != []:
        #     print("Not")
        # for a in Test.objects.filter(name="Tlezip"):
        #     print(a.name)

    # def test_is_display(self):
    #     response = Test.objects.create(name="Math Test", 
    #                       is_display = False,
    #                       )
        # filt = {'name': 'Tlezip'}
        # getdata = requests.get('http://localhost:8000/api/test/', data=filt)
        # print(getdata.content)
    #     print("123")
    #     # assert response in 




    # def test_csrf_exempt_by_default(self):
    #     """
    #     By default, the test client is CSRF exempt.
    #     """
    #     User.objects.create_user('example', 'example@example.com', 'password')
    #     self.client.login(username='example', password='password') #general user
    #     response = self.client.post('/home/')
    #     assert response.status_code == 200

    # def test_error_unrol(self):
    #     User.objects.create_user('example', 'example@example.com', 'password')
    #     self.client.login(username='example', password='password') #general user
    #     response = self.client.post('/dashboard/')
    #     assert response.status_code != 200


    # def test_overview_toomuch_default(self):
    # # """
    # # By default, the test client is CSRF exempt.
    # # """
    #     response = self.client.post('/createtest/', {'name': 'Math Test', 
    #                                 'typetest' : "Choice", 
    #                                 'category' : "AIS Products", 
    #                                 'overview' : "This is overviewdsfqwertyuiop[asdfghjkl;zxcvbnm,./azqwsxedcrfvtgbyhnujmik,ol.p;/['zqawsxedcrfvtgbyhnujmik,ol.p;/['aqswxedcrfvtgbyhnjmk,ol.p;/[azqswdefrgthyjumki,lo.;p/'[xscdefrgthyujki,lo.;p", 
    #                                 'provider' : "Tlezip",
    #                                 'conndition' : "This is condition detail",
    #                                 'max_submit' : 5, 
    #                                 'limit' : 0, 
    #                                 'expired' : 0,
    #                                 'descripe' : "This is descripe",}, format='json')
    #     print(response.content)
    #     assert response.status_code != 200 


# class TestCase_CreateOnlyrequire(TestCase):
    
#     def setUp(self):
#         self.client = APIClient()

#     def test_csrf_exempt_by_default(self):
#     # """
#     # By default, the test client is CSRF exempt.
#     # """
#         response = self.client.post('/createtest/', {'name': 'Math Testfglkfd;lgdfklgkfdl;gkl;fdkgl;fdklg;fdlgkfldkg;lkfd;lgkdlf;kgl;fdkgl;dkfl;gl;dlfgdflg'}, format='json')
#         assert response.status_code != 200 




# c = Client()
# response = c.post('/createtest/', {'name': 'Math Test', 
# 									'typetest' : "Choice", 
#  									'category' : "AIS Products", 
#  									'overview' : "This is overview", 
#  									'provider' : "Tlezip",
#  									'conndition' : "This is condition detail",
#  									'max_submit' : 5, 
#  									'limit' : 0, 
#  									'expired' : 0,
#  									'descripe' : "This is descripe",})
# response.status_code
# response = c.get('/test/1/')
# response.content


# class TestCase_Create(APITestCase):
# 	def test_creat_test(self):
# 		self.client.post('/createtest/',{'name' : "Math Test",
# 									'typetest' : "Choice", 
# 									'category' : "AIS Products", 
# 									'overview' : "This is overview", 
# 									'provider' : "Tlezip",
# 									'conndition' : "This is condition detail",
# 									'max_submit' : 5, 
# 									'limit' : 0, 
# 									'expired' : 0,
# 									'descripe' : "This is descripe",
# 									}, format='json')
#	def test_check_test(self):

	

# factory = APIRequestFactory()
# request = factory.post('/legotest/', {'name' : "Math Test",
# 									'typetest' : "Choice", 
# 									'category' : "AIS Products", 
# 									'overview' : "This is overview", 
# 									'provider' : "Tlezip",
# 									'conndition' : "This is condition detail",
# 									'max_submit' : 5, 
# 									'limit' : 0, 
# 									'expired' : 0,
# 									'descripe' : "This is descripe",
# 									}, format='json')

# request = factory.get('/letotest/')
# request.name = "Math Test2"
# assert request.name == "Math Test2"
	

# class legotestTestCase(TestCase):

# 	def setUp(self):
# 		Test.objects.create(name="Math Test", 
# 							typetest="Choice", 
# 							category="AIS Products", 
# 							overview="this is overview", 
# 							provider="Tlezip", 
# 							condition="This is condition detail", 
# 							max_submit=5, 
# 							limit=0,
# 							expired=0, 
# 							descripe="this is descripe",
# 							)

# 	def test_Test_pull(self):
# 		a = Test.objects.get(name="Math Test")
# 		self.assertEqual(a.overview, "this is overview")

# 	def test_Test_update(self):
# 		b = Test.objects.get(name="Math Test")
# 		b.name = "Math Test2"
# 		b.save()


