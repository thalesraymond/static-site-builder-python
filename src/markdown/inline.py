import re

from src.models.text_node import TextNode, TextType


def extract_markdown_images(text):
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    matches = re.findall(image_pattern, text)
    return matches


def extract_markdown_links(text):
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(link_pattern, text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise ValueError(
                f"Delimiter pair '{delimiter}' not found in text node: '{node.text}'"
            )

        split_node_delimiter = node.text.split(delimiter)

        for i in range(len(split_node_delimiter)):
            if split_node_delimiter[i] == "":
                continue

            if i % 2 == 1:
                split_nodes.append(TextNode(split_node_delimiter[i], text_type))
            else:
                split_nodes.append(TextNode(split_node_delimiter[i], TextType.TEXT))

    return split_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # If the node is not a TEXT type, we don't need to split it
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)
        # If no images are found, just add the original node
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        # Iterate through each image found in the text
        for image in images:
            # Split the text by the image markdown, limiting to 1 split at a time
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            # Add the text before the image as a TEXT node
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            # Add the image itself as an IMAGE node
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )

            # The remaining text becomes the new original_text for the next iteration
            original_text = sections[1]

        # After processing all images, add any remaining text
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # If the node is not a TEXT type, we don't need to split it
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)
        # If no links are found, just add the original node
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        # Iterate through each link found in the text
        for link in links:
            # Split the text by the link markdown, limiting to 1 split at a time
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            # Add the text before the image as a TEXT node
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            # Add the link itself as a LINK node
            new_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1],
                )
            )

            # The remaining text becomes the new original_text for the next iteration
            original_text = sections[1]

        # After processing all images, add any remaining text
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    # use all spliting functions to convert text to textnodes/images/links
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
