import unittest

from src.models.html_node import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(
            "p",
            "Hello, world!",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HtmlNode("p", "Hello, world!", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_error(self):
        node = HtmlNode("p", "Hello, world!")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HtmlNode("p", "Hello, world!", None, {"class": "greeting"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, Hello, world!, children: None, {'class': 'greeting'})",
        )

    def test_values(self):
        node = HtmlNode("div", "I am a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I am a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)


if __name__ == "__main__":
    unittest.main()
