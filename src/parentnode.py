from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f"<{self.tag} {self.props}> with {len(self.children)} children"
    
    def to_html(self):
        if self.children is None:
            raise ValueError("Children cannot be None")
          
        if self.tag is None:
            raise ValueError("Tag cannot be None") 
          
        props_html = self.props_to_html()
        
        children_html = "".join(child.to_html() for child in self.children)
        
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"