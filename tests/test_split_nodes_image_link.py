import unittest

from src.markdown.inline import split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType


class TestSplitNodesImageLink(unittest.TestCase):
    def test_split_images(self):

        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_image_at_start(self):
        node = TextNode(
            "![image](https://www.example.com/image.png) is an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.com/image.png"),
                TextNode(" is an image", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_at_end(self):
        node = TextNode(
            "This is an image: ![image](https://www.example.com/image.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is an image: ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This text has no images.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                node,
            ],
            new_nodes,
        )

    def test_split_images_non_text_node(self):
        node = TextNode(
            "This is a bold node",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                node,
            ],
            new_nodes,
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_split_link_single(self):
        node = TextNode(
            "[link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )

    def test_split_link_at_start(self):
        node = TextNode(
            "[link](https://www.example.com) is a link",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" is a link", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_end(self):
        node = TextNode(
            "This is a link: [link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a link: ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode(
            "This text has no links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                node,
            ],
            new_nodes,
        )

    def test_split_links_non_text_node(self):
        node = TextNode(
            "This is a bold node",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                node,
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
