import unittest
from crawl import normalize_url

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://corviamarket.org/"
        output_url = normalize_url(input_url)
        expected = "corviamarket.org"
        self.assertEqual(output_url, expected)

    def test_normalize_url_with_path(self):
        input_url = "https://corviamarket.org/path"
        output_url = normalize_url(input_url)
        expected = "corviamarket.org/path"
        self.assertEqual(output_url, expected)

    def test_normalize_url_with_multiple_path_segments(self):
        input_url = "https://corviamarket.org/path/to/page/"
        output_url = normalize_url(input_url)
        expected = "corviamarket.org/path/to/page"
        self.assertEqual(output_url, expected)
if __name__ == "__main__":
    unittest.main()