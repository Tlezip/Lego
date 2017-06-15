from django.test import TestCase
from rest_framework.test import APIRequestFactory
from legotest.models import Test
from rest_framework.test import APITestCase

# Create your tests here.

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


