import os

from django.test import TestCase
from django.urls import reverse_lazy
from django.conf import settings


class TestPersonListView(TestCase):
    def setUp(self):
        self.path = reverse_lazy('fileupload:person_list')

    def test_list(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)


class TestPersonCreateView(TestCase):
    def setUp(self):
        self.path = reverse_lazy('fileupload:person_create')

    def test_create(self):
        media_root = settings.MEDIA_ROOT
        tmp_file = os.path.join(media_root, 'test/tmp.txt')
        with open(tmp_file, 'r') as fp:
            data = {'name': 'Hello-World', 'data_file': fp}
            response = self.client.post(path=self.path, data=data)
            self.assertEqual(response.status_code, 201)


class TestPersonListCreateView(TestCase):
    def setUp(self):
        self.path = reverse_lazy('fileupload:person_list_create')

    def test_list(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        media_root = settings.MEDIA_ROOT
        tmp_file = os.path.join(media_root, 'test/tmp.txt')
        with open(tmp_file, 'r') as fp:
            data = {'name': 'Hello-World', 'data_file': fp}
            response = self.client.post(path=self.path, data=data)
            self.assertEqual(response.status_code, 201)
