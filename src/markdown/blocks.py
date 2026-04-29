from enum import Enum


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"
    
    
# def markdown_block_to_html_node(block):
#     block_type = block_to_block_type(block)
#     if block_type == BlockType.heading:
#         return heading_block_to_html_node(block)
#     elif block_type == BlockType.code:
#         return code_block_to_html_node(block)
#     elif block_type == BlockType.quote:
#         return quote_block_to_html_node(block)
#     elif block_type == BlockType.unordered_list:
#         return unordered_list_block_to_html_node(block)
#     elif block_type == BlockType.ordered_list:
#         return ordered_list_block_to_html_node(block)
#     else:
#         return paragraph_block_to_html_node(block)

# def heading_block_to_html_node(block):
    

def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        if line.strip() == "":
            continue
        blocks.append(line.strip())
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BlockType.heading

    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.code

    if block.startswith("```") and block.endswith("```") and len(block) >= 6:
        return BlockType.code

    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.paragraph
        return BlockType.quote

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.paragraph
        return BlockType.unordered_list

    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.paragraph
        return BlockType.unordered_list

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.paragraph
            i += 1
        return BlockType.ordered_list

    return BlockType.paragraph
