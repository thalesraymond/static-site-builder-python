def markdown_to_blocks(markdown):
  lines = markdown.split("\n\n")
  blocks = []
  
  for line in lines:
    if line.strip() == "":
      continue  # Skip empty lines

    blocks.append(line.strip())
    

  return blocks
  