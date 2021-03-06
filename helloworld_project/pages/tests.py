from django.test import SimpleTestCase, TestCase
from .models import Post

# Create your tests here.
class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

#     def test_admin_page_status_code(self):
#         response = self.client.get('/admin')
#         self.assertEqual(response.status_code, 200)
#
#
# class PostTestCase(TestCase):
#     def set_up(self):
#         Post.objects.create(text='just a test')
#
#     def test_text_content(self):
#         post = Post.objects.get(id=1)
#         expected_object_name = f'{post.text}'
#         self.assertEqual(expected_object_name, 'just a test')
