from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  split_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      split_nodes.append(node)
      continue

    if node.text.count(delimiter) % 2 != 0:
      raise ValueError(f"Delimiter pair '{delimiter}' not found in text node: '{node.text}'")

    split_node_delimiter = node.text.split(delimiter)
    
    for i in range(len(split_node_delimiter)):
      if split_node_delimiter[i] == "":
        continue
      
      if i % 2 == 1:
        split_nodes.append(TextNode(split_node_delimiter[i], text_type))
      else:
        split_nodes.append(TextNode(split_node_delimiter[i], TextType.TEXT))
    
  
  return split_nodes
    