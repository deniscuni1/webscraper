import unittest
from extract_page_data import extract_page_data, ExtractedData

class TestExtract(unittest.TestCase):
    def test_extract_page_data(self):
        input_url = "https://crawler-test.com"
        input_html =  """<html><body>
        <h1>Test Title</h1>
        <p>This is the first paragraph.</p>
        <a href="/link1">Link 1</a>
        <img src="/image1.jpg" alt="Image 1">
        </body></html>"""
        output = extract_page_data(input_html, input_url)
        expected = {
        "url": "crawler-test.com",
        "heading": "Test Title",
        "first_paragraph": "This is the first paragraph.",
        "outgoing_links": ["crawler-test.com/link1"],
        "image_urls": ["crawler-test.com/image1.jpg"],
        }
        self.assertEqual(output, expected)
        print("it works")

    def test_extract_page_data_multiple_links_and_images(self):
        input_url = "https://crawler-test.com"
        input_html = """<html><body>
        <h1>Another Title</h1>
        <p>Another paragraph.</p>
        <a href="/link1">Link 1</a>
        <a href="/link2">Link 2</a>
        <img src="/image1.jpg" alt="Image 1">
        <img src="/image2.jpg" alt="Image 2">
        </body></html>"""
        output = extract_page_data(input_html, input_url)
        expected = {
        "url": "crawler-test.com",
        "heading": "Another Title",
        "first_paragraph": "Another paragraph.",
        "outgoing_links": ["crawler-test.com/link1", "crawler-test.com/link2"],
        "image_urls": ["crawler-test.com/image1.jpg", "crawler-test.com/image2.jpg"],
        }
        self.assertEqual(output, expected)

    def test_extract_page_data_trailing_slash_url(self):
        input_url = "https://crawler-test.com/"
        input_html = """<html><body>
        <h1>Trailing Slash</h1>
        <p>Paragraph text.</p>
        <a href="/link1">Link 1</a>
        <img src="/image1.jpg" alt="Image 1">
        </body></html>"""
        output = extract_page_data(input_html, input_url)
        expected = {
        "url": "crawler-test.com",
        "heading": "Trailing Slash",
        "first_paragraph": "Paragraph text.",
        "outgoing_links": ["crawler-test.com/link1"],
        "image_urls": ["crawler-test.com/image1.jpg"],
        }
        self.assertEqual(output, expected)