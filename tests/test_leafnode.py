import unittest

from src.models.html_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        self.assertEqual(node.to_html(), '<p class="greeting">Hello, world!</p>')

    def test_to_html_no_props(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Hello, world!, children: None, {'class': 'greeting'})",
        )


if __name__ == "__main__":
    unittest.main()
