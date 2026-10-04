import unittest
from get_images_from_html import get_images_from_html
class TestImage(unittest.TestCase):
    def test_get_images_from_html(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        output = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png"]
        self.assertEqual(output, expected)

    def test_get_images_from_html_multiple(self):
        input_url = "https://crawler-test.com"
        input_body = '<html><body><img src="/logo.png"><img src="/banner.jpg"></body></html>'
        output = get_images_from_html(input_body, input_url)
        expected = ["https://crawler-test.com/logo.png", "https://crawler-test.com/banner.jpg"]
        self.assertEqual(output, expected)

    def test_get_images_from_html_none(self):
        input_url = "https://crawler-test.com"
        input_body = "<html><body><p>No images here.</p></body></html>"
        output = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(output, expected)
