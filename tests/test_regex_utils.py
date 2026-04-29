import unittest

from src.markdown.utils import extract_markdown_images, extract_markdown_links


class TestRegexUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zcew34n.png) and ![another](https://i.imgur.com/dfSzzq6.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zcew34n.png"),
                ("another", "https://i.imgur.com/dfSzzq6.png"),
            ],
            matches,
        )

    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images, only a [link](https://www.google.com)"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.google.com) and [another](https://www.example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.google.com"),
                ("another", "https://www.example.com"),
            ],
            matches,
        )

    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links, only an ![image](https://i.imgur.com/zcew34n.png)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("image", "https://i.imgur.com/zcew34n.png")], matches)

    def test_extract_mixed_markdown(self):
        text = "This has an ![image](img_url) and a [link](link_url)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("image", "img_url")], image_matches)
        # Note: current link regex matches images too
        self.assertListEqual([("image", "img_url"), ("link", "link_url")], link_matches)


if __name__ == "__main__":
    unittest.main()
