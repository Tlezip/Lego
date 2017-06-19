from django.test import TestCase
from rest_framework.test import APIClient
from legocourse.models import Course
from legocourse.models import Section


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_1 = Course.objects.create(name='course1', is_display=True)
        self.course_2 = Course.objects.create(name='course2', is_display=True)
        self.course_3 = Course.objects.create(name='course3', is_display=False)
        self.section_1 = Section.objects.create(course=self.course_1, name='section1')

    def test_get(self):
        request = self.client.get('/api/course/')
        assert request.status_code == 200

    def test_post(self):
        request = self.client.post('/api/course/', {'name': 'due'}, format='json')
        assert request.status_code == 403

    def test_put(self):
        request = self.client.put('/api/course/', {'name': 'due'}, format='json')
        assert request.status_code == 403

    def test_patch(self):
        request = self.client.patch('/api/course/', {'name': 'due'}, format='json')
        assert request.status_code == 403

    # def test_get_display(self):
    #     response = self.client.get('/api/course/')
    #     if(self.course_1.is_display == True):
    #         assert response.status_code == 200
    #     else:
    #         assert response.status_code == 404
    #     print(response.json())

    def test_get_section(self):
        response = self.client.get('/api/course/')
        if(Course.objects.filter(section__isnull=False).count() == 0):
            assert response.status_code == 200
