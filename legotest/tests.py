from django.test import TestCase,Client
from rest_framework.test import APIRequestFactory
from legotest.models import Test
from rest_framework.test import APITestCase,APIClient
from django.contrib.auth.models import User
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

    def test_is_display(self):
        Test.objects.create(name="Math Test", 
                          typetest="Choice", 
                          category="AIS Products", 
                          overview="this is overview", 
                          provider="Tlezip", 
                          condition="This is condition detail", 
                          max_submit=5, 
                          limit=0,
                          expired=0, 
                          descripe="this is descripe",
                          is_display = False,
                          )




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


