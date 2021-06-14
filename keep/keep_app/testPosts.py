from django.test import TestCase
from keep_app.models import KeepApp

from django.urls import reverse
import json
from rest_framework import status


class PostTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {
            "title": "New Task with due date",
            "status": False,
            "due_date": "2021-06-14"
        }

        self.invalid_payload = {
            "title": "",
            "status": False,
            "due_date": "2021-06-14"
        }

    def testPost(self):
        post = KeepApp(title="Test Title", status=True)
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.status, True)

    def test_create_valid_task(self):
        response = self.client.post(
            reverse('todo-create-update'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = self.client.post(
            reverse('todo-create-update'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_task_fail(self):
        response = self.client.post(
            reverse('todo-create-update'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
