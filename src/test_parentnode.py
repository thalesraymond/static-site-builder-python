import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.props, {"class": "container"})

    def test_init_no_children(self):
        node = ParentNode("div", None)
        self.assertEqual(node.children, [])

    def test_add_child(self):
        node = ParentNode("div", [])
        child = LeafNode("p", "Hello")
        node.add_child(child)
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0], child)

    def test_str(self):
        node = ParentNode("div", [LeafNode("p", "Hello")], {"class": "test"})
        self.assertEqual(str(node), "<div {'class': 'test'}> with 1 children")

    def test_to_html_simple(self):
        node = ParentNode("div", [LeafNode("p", "Hello")])
        self.assertEqual(node.to_html(), "<div><p>Hello</p></div>")

    def test_to_html_multiple_children(self):
        children = [
            LeafNode("p", "Hello"),
            LeafNode("span", "World")
        ]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), "<div><p>Hello</p><span>World</span></div>")

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<div class="container" id="main"><p>Hello</p></div>')

    def test_to_html_nested(self):
        inner = ParentNode("span", [LeafNode(None, "Hello")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span>Hello</span></div>")

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_children_none(self):
        node = ParentNode("div", [LeafNode("p", "Hello")])
        node.children = None  # Manually set to None to test
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()