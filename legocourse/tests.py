from django.test import TestCase
from rest_framework.test import APIClient


class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get(self):
        request = self.client.get('/api/course/')
        assert request.status_code == 200

    def test_post(self):
        request = self.client.post('/api/course/')
        print(request.status_code)
        assert request.status_code == 405

# from django.test import TestCase
# from legocourse.models import *
# from django.contrib.contenttypes.models import ContentType
#
#
# text_length_200 = ''
# text_length_250 = ''
#
# for i in range(0,300):
#     text_length_200 += 'a'
#
# for i in range(0,300):
#     text_length_250 += 'b'
#
# class CourseTestCase(TestCase):
#     video = ContentType.objects.get(model='video')
#     audio = ContentType.objects.get(model='audio')
#     def setUp(self):
#         _course = Course(name="due", overview=text_length_250)
#         _course.save()
#
#         section_1 = Section.objects.create(course=_course, name=text_length_200)
#         section_2 = Section.objects.create(course=_course, name=text_length_200)
#         Section.objects.create(course=_course, name=text_length_200)
#
#         Material.objects.create(section=section_1 , content_type=self.video ,content=15)
#         Material.objects.create(section=section_2, content_type=self.audio, content=16)
#
#     def test_section_sort(self):
#         _section = Section.objects.get(pk=2)
#         _material_1 = Material.objects.get(pk=1)
#         _material_2 = Material.objects.get(pk=2)
#         self.assertEqual(_material_1.content_type, self.video)
#         self.assertEqual(_material_2.content_type, self.audio)
#         self.assertEqual(_section.sort, 2)