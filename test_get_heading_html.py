import unittest
from get_heading_from_html import get_heading_from_html

class TestHtml(unittest.TestCase):
    def testParagraph(self):
        input_html = """<html><body>
                            <p>Outside paragraph.</p>
                            <main>
                                <p>Main paragraph.</p>
                            </main>
                        </body></html>"""
        expected = ["Outside paragraph.", "Main paragraph."]
        output = get_heading_from_html(input_html)
        self.assertEqual(expected, output)
    def test_get_heading_from_html_basic(self):
        input_body = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_heading_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_with_paragraph(self):
        input_body = "<html><body><h1>Test Title</h1><p>First paragraph.</p></body></html>"
        actual = get_heading_from_html(input_body)
        expected = ("Test Title", ["First paragraph."])
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_empty(self):
        input_body = "<html><body></body></html>"
        actual = get_heading_from_html(input_body)
        expected = []
        self.assertEqual(actual, expected)