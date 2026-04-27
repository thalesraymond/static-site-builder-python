import unittest

from block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

  def test_markdown_to_blocks_excessive_newlines(self):
    md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

  def test_markdown_to_blocks_whitespace(self):
    md = "  This is a block with leading and trailing spaces  \n\n   Another block   "
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is a block with leading and trailing spaces",
            "Another block",
        ],
    )

  def test_markdown_to_blocks_single_block(self):
    md = "Just a single block of text."
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        ["Just a single block of text."],
    )

  def test_markdown_to_blocks_empty(self):
    md = "  \n\n  "
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [])

  def test_markdown_to_blocks_multiline(self):
    md = "Line 1\nLine 2\nLine 3"
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        ["Line 1\nLine 2\nLine 3"],
    )

    

if __name__ == "__main__":
  unittest.main()