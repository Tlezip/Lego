from django.test import TestCase
from rest_framework.test import APIClient
from legocourse.models import *
from legocourse.serializers import CourseSerializer
from django.contrib.contenttypes.models import ContentType


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        ctype = ContentType.objects.get(model='video')
        self.course = Course.objects.create(name='course1', is_display=False)
        # self.material = Material.objects.create(content_type=ctype, section=self.section)

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
        course1 = CourseSerializer(self.course)
        response = self.client.get('/api/course/')
        assert course1.data not in response.data

        self.course.is_display = True
        self.course.save()

        course1 = CourseSerializer(self.course)
        response = self.client.get('/api/course/')
        assert course1.data in response.data

    def test_get_section(self):
        pass