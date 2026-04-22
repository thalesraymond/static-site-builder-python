from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType


def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextType.TEXT:
      return LeafNode(None, text_node.text)
    case TextType.BOLD:
      return ParentNode("b", [LeafNode(None, text_node.text)])
    case TextType.ITALIC:
      return ParentNode("i", [LeafNode(None, text_node.text)])
    case TextType.CODE:
      return ParentNode("code", [LeafNode(None, text_node.text)])
    case TextType.LINK:
      return ParentNode("a", [LeafNode(None, text_node.text)], {"href": text_node.url})
    case TextType.IMAGE:
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    case _:
      raise ValueError(f"Unknown text type: {text_node.text_type}")