import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):

        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Hello, world!")

    def test_text_node_to_html_node_bold(self):

        text_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Hello, world!</b>")

    def test_text_node_to_html_node_italic(self):

        text_node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Hello, world!</i>")

    def test_text_node_to_html_node_code(self):

        text_node = TextNode("print('Hello, world!')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>print('Hello, world!')</code>")

    def test_text_node_to_html_node_link(self):

        text_node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(), '<a href="https://example.com">Click here</a>'
        )

    def test_text_node_to_html_node_image(self):

        text_node = TextNode(
            "An image", TextType.IMAGE, "https://example.com/image.png"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://example.com/image.png" alt="An image"></img>',
        )


if __name__ == "__main__":
    unittest.main()
