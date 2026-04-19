from textnode import TextNode, TextType


print("Hello World!")

def main():
    print("This is the main function.")
    node = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")
    
    print(node)
    

if __name__ == "__main__":
    main()