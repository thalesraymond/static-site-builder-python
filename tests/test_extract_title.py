import unittest
from src.markdown.converter import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_with_extra_spaces(self):
        md = "#    Hello World   "
        self.assertEqual(extract_title(md), "   Hello World")

    def test_extract_title_not_first_block(self):
        md = """
This is a paragraph.

# The Real Title
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_extract_title_no_title(self):
        md = "This is just a paragraph."
        self.assertIsNone(extract_title(md))

    def test_extract_title_multiple_h1(self):
        md = """
# First Title

# Second Title
"""
        self.assertEqual(extract_title(md), "First Title")

    def test_extract_title_other_headings(self):
        md = "## This is an H2"
        self.assertIsNone(extract_title(md))

if __name__ == "__main__":
    unittest.main()
