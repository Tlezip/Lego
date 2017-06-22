from django.test import TestCase,Client
from rest_framework.test import APIRequestFactory
from legotest.models import *
from rest_framework.test import APITestCase,APIClient
from django.contrib.auth.models import User
from django.http import HttpRequest
from legotestquestion.models import *
import requests
import urllib
import json
from django.core import serializers
from legotest.serializer import TestSerializer
# Create your tests here.

class TestCase_Create(TestCase):
	
    def setUp(self):
        self.client = APIClient()
        self.test = Test.objects.create(name='Tlezip', is_display=True)
        self.test2 = Test.objects.create(name='qwerty', is_display=True)
        self.section = Section.objects.create(name='Section1', test=self.test)
        self.realquestion = legotestquestion.Question.objects.create(text='qwerty',answer='yes')
        self.question = Question.objects.create(sectionid=self.section, questionid=self.realquestion.id)
        self.all = Test.objects.all()
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

    def test_is_display(self):
        self.test.is_display = True
        self.test.save()
        c = TestSerializer(self.test)
        response = self.client.get('/api/test/')
        assert c.data in response.data

        self.test.is_display = False
        self.test.save()
        c = TestSerializer(self.test)
        assert c.data not in response.data

    def test_section(self):
        response = self.client.get('/api/test/2/')
        # print(response.json()['section'])
        if response.json()['section'] == []:
            assert response.json()['is_display'] == False
        section2 = Section.objects.create(name='Section2', test=self.test2)
        assert response.json()['is_display'] == True or False

    def test_Question(self):
        reponse = self.client.get('/api/test/')
        # queryset = Test.objects.filter(id=self.test.id).select_releated('content')
        # print(self.test2.content)
        # if self.test2.section == []:
        #     print("Error")
        # print(self.test2)
        # c = TestSerializer(self.test2)
        # print(c.data)
        # results = serializers.serialize('json', response)
        # print(results.id)
        # a = Test.objects.filter(section=None)
        # for x in a:
            # assert x.is_display == False


        # if len(response.data) == 0:
        #     assert not isinstance(False, Test)
        #     for x in self.all:
        #         print(x.name)
        #         x.is_display = False
        #         x.save()
        # else:
        #     print("456")
        
        # if a != []:
        #     print("Not")
        # for a in Test.objects.filter(name="Tlezip"):
        #     print(a.name)

    # def test_is_display(self):
    #     response = Test.objects.create(name="Math Test", 
    #                       is_display = False,
    #                       )
        # filt = {'name': 'Tlezip'}
        # getdata = requests.get('http://localhost:8000/api/test/')
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