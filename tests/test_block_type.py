import unittest

from src.markdown.blocks import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_block_types(self):
        self.assertEqual(BlockType.paragraph.value, "paragraph")
        self.assertEqual(BlockType.heading.value, "heading")
        self.assertEqual(BlockType.code.value, "code")
        self.assertEqual(BlockType.quote.value, "quote")
        self.assertEqual(BlockType.unordered_list.value, "unordered_list")
        self.assertEqual(BlockType.ordered_list.value, "ordered_list")

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("## heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("### heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("#### heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("##### heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("###### heading"), BlockType.heading)
        self.assertEqual(block_to_block_type("####### heading"), BlockType.paragraph)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.code)
        self.assertEqual(block_to_block_type("```code```"), BlockType.code)
        self.assertEqual(block_to_block_type("``code``"), BlockType.paragraph)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> quote"), BlockType.quote)
        self.assertEqual(block_to_block_type("> line 1\n> line 2"), BlockType.quote)
        self.assertEqual(block_to_block_type("> line 1\nline 2"), BlockType.paragraph)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1"), BlockType.unordered_list)
        self.assertEqual(block_to_block_type("* item 1"), BlockType.unordered_list)
        self.assertEqual(
            block_to_block_type("- item 1\n- item 2"), BlockType.unordered_list
        )
        self.assertEqual(
            block_to_block_type("* item 1\n* item 2"), BlockType.unordered_list
        )
        self.assertEqual(block_to_block_type("- item 1\nitem 2"), BlockType.paragraph)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item 1"), BlockType.ordered_list)
        self.assertEqual(
            block_to_block_type("1. item 1\n2. item 2"), BlockType.ordered_list
        )
        self.assertEqual(
            block_to_block_type("1. item 1\n3. item 2"), BlockType.paragraph
        )
        self.assertEqual(block_to_block_type("2. item 1"), BlockType.paragraph)

    def test_block_to_block_type_paragraph(self):
        self.assertEqual(
            block_to_block_type("this is a paragraph"), BlockType.paragraph
        )
        self.assertEqual(block_to_block_type("#heading"), BlockType.paragraph)


if __name__ == "__main__":
    unittest.main()
