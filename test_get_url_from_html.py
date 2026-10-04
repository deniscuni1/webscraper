import unittest
from get_url_from_html import get_urls_from_html

class TestUrl(unittest.TestCase):
    def test_urls(self):
        input_urls = '<html><body><a href="https://crawler-test.com"><span>Boot.dev</span></a></body></html>'
        output = get_urls_from_html(input_urls)
        expected = ["https://crawler-test.com"]
        self.assertEqual(output, expected)

    def test_urls_multiple(self):
        input_urls = '<html><body><a href="/link1">One</a><a href="/link2">Two</a></body></html>'
        output = get_urls_from_html(input_urls)
        expected = ["/link1", "/link2"]
        self.assertEqual(output, expected)

    def test_urls_none(self):
        input_urls = "<html><body><p>No links here.</p></body></html>"
        output = get_urls_from_html(input_urls)
        expected = []
        self.assertEqual(output, expected)