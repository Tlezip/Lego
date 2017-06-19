from django.test import TestCase
from rest_framework.test import APIClient
from legocourse.models import Course
from legocourse.models import Section
from legocourse.serializers import CourseSerializer


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name='course', is_display=True)
        self.section = Section.objects.create(course=self.course, name='section')

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

    def test_get_display(self):
        temp = CourseSerializer(self.course)
        response = self.client.get('/api/course/')
        if(self.course.is_display == False):
            assert temp.data in response.data
            print(response.json())

        else:
            assert temp.data not in response.data

    # def test_get_section(self):
    #     response = self.client.get('/api/course_detail/')
    #     if(Course.objects.filter(section__isnull=False).count() == 0):
    #         assert response.status_code == 200
